import os
import sys
import requests
import datetime
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageGrab
import tkinter as tk
from tkinter import simpledialog, Tk, Button, messagebox, Entry, Label
import threading
import json
import winreg
import time

# Firebase Config (Replace with your own Firebase config)
firebase_config = {
    # Your config #
}

# Normal Python execution version of get_resource_path

# def get_resource_path(relative_path):
#     """Get the absolute path to the resource during normal Python execution."""
#     return os.path.join(os.path.abspath("."), relative_path)

# Uncomment the following get_resource_path for Nuitka or PyInstaller versions

def get_resource_path(relative_path):
    """Get the absolute path to the resource for PyInstaller or Nuitka execution."""
    try:
        # PyInstaller stores files in _MEIPASS during execution
        base_path = sys._MEIPASS
    except AttributeError:
        # For normal Python execution
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Registry-related functions
def save_username_to_registry(username):
    """Save the username to the Windows Registry."""
    try:
        reg_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\wwpt")
        winreg.SetValueEx(reg_key, "Username", 0, winreg.REG_SZ, username)
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"Failed to save username to registry: {e}")

def get_username_from_registry():
    """Retrieve the username from the Windows Registry."""
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\wwpt", 0, winreg.KEY_READ)
        username, _ = winreg.QueryValueEx(reg_key, "Username")
        winreg.CloseKey(reg_key)
        return username
    except FileNotFoundError:
        return None  # Key does not exist yet
    except Exception as e:
        print(f"Failed to retrieve username from registry: {e}")
        return None

def get_username():
    """Function to get the username from the registry and prompt the user if it's not set."""
    username = get_username_from_registry()
    if username is None:
        return ask_for_username()  # Prompt for a new username if it's not in the registry
    return username

def ask_for_username():
    """Prompt the user for a username, check its existence in Firestore, and save it."""
    while True:
        root = Tk()
        root.withdraw()  # Hide the main window
        username = simpledialog.askstring("Input", "Enter your username (or click Cancel to exit):", parent=root)
        root.destroy()

        if username is None:  # If the user clicks "Cancel" or closes the window
            messagebox.showinfo("Exit", "No username provided. Exiting the application.")
            quit_program(None, None)
            return None  # Exit the loop and function

        if username:
            # Check if the username exists in Firestore
            if check_username_exists(username):
                save_username_to_registry(username)  # Save the username to the registry
                return username
            else:
                messagebox.showerror("Error", "Username doesn't exist.")
        else:
            messagebox.showerror("Error", "Username cannot be empty.")

def check_username_exists(username):
    """Check if a username collection exists in Firestore via REST API."""
    url = f"{firebase_config['databaseURL']}/{username}?key={firebase_config['apiKey']}"
    response = requests.get(url)

    if response.status_code == 200:
        documents = response.json().get('documents')
        return bool(documents)  # Return True if documents exist, else False
    else:
        return False

def edit_username():
    """Function to edit the username."""
    username = ask_for_username()
    if username:
        save_username_to_registry(username)

def quit_program(icon, item):
    """Function to quit the application."""
    icon.stop()
    os._exit(0)  # Ensure the program exits

def save_to_firestore(username, detected_text):
    """Function to save text results to Firestore using REST API."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    url = f"{firebase_config['databaseURL']}/{username}/save?key={firebase_config['apiKey']}"

    data = {
        "fields": {
            "plate_number": {"stringValue": detected_text},
            "timestamp": {"stringValue": current_time}
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.patch(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print(f"Data saved to Firestore under '{username}' collection with document ID 'save'.")
    else:
        messagebox.showerror("Error", f"Failed to save data to Firestore: {response.content}")

def save_text_input(text, current_username_label, save_label):
    """Function to handle saving the user input text to Firestore and display 'Saved'."""
    username = get_username()
    if username:
        try:
            number = int(text)  # Convert the input text to an integer
            if 0 <= number <= 240:
                save_to_firestore(username, str(number) + "/240")
                # Update the current username label
                current_username_label.config(text=f"Current User: {username}")
                # Show "Saved" text for 2 seconds
                save_label.config(text="Saved")
                save_label.after(2000, lambda: save_label.config(text=""))
            else:
                messagebox.showerror("Error", "Input out of range! Please enter a number between 0 and 240.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid integer.")
    else:
        messagebox.showerror("Error", "No username found. Please set a username.")

def on_closing(settings_window):
    """Function to handle window closing event."""
    settings_window.destroy()

def show_settings_menu():
    """Function to show the settings window with options."""
    settings_window = tk.Tk()
    settings_window.title("Settings Menu")

    # Set the window size (e.g., 300x200 pixels)
    settings_window.geometry("300x220")  # Adjust width and height as needed

    # Bind the closing event to handle window close
    settings_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(settings_window))

    # Display the current username at the top
    current_username = get_username()
    current_username_label = Label(settings_window, text=f"Current User: {current_username}")
    current_username_label.pack(pady=10)

    # Add a button to edit the username
    edit_username_button = Button(settings_window, text="Edit Username", command=lambda: edit_username_and_update_label(current_username_label))
    edit_username_button.pack(pady=5)

    # Input text box for user input
    input_label = tk.Label(settings_window, text="Enter plates:")
    input_label.pack(pady=5)

    input_text = Entry(settings_window, justify='center')
    input_text.pack(pady=5)

    # Save button and saved label
    save_button = Button(settings_window, text="Save", command=lambda: save_text_input(input_text.get(), current_username_label, save_label))
    save_button.pack(pady=5)

    # "Saved" label that appears after saving
    save_label = Label(settings_window, text="", fg="green")
    save_label.pack()

    settings_window.mainloop()

def edit_username_and_update_label(current_username_label):
    """Function to edit the username and update the label with the new username."""
    edit_username()
    current_username = get_username()
    current_username_label.config(text=f"Current User: {current_username}")

def create_tray_icon():
    """Function to create the system tray icon."""
    icon_image = Image.open(get_resource_path("icon.png"))  # Replace with a path to your tray icon image

    menu = (
        item('Settings', lambda icon, item: show_settings_menu()),
        item('Quit', quit_program)
    )

    icon = pystray.Icon("plate_detector", icon_image, "Plate Detector", menu)
    icon.run()

if __name__ == "__main__":
    username = get_username()

    if username:
        print(f"Welcome, {username}!")
        # If username exists, start in tray
        tray_thread = threading.Thread(target=create_tray_icon)
        tray_thread.daemon = True
        tray_thread.start()
        tray_thread.join()  # Keep the main thread alive to run the tray icon
    else:
        # If no username, prompt and then show settings window
        print("No username provided. Exiting.")
        quit_program(None, None)
