import os
import sys
import firebase_admin
from firebase_admin import credentials, firestore
import datetime
from paddleocr import PaddleOCR
import cv2
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageGrab
import tkinter as tk
from tkinter import simpledialog, Tk, Button, messagebox
import threading

# Determine the path to the service account JSON file
if getattr(sys, 'frozen', False):
    # If the application is run as a bundled executable, the JSON file will be in the temp directory
    base_path = sys._MEIPASS
else:
    # If run in a normal Python environment, assume the JSON file is in the current directory
    base_path = os.path.abspath(".")

json_path = os.path.join(base_path, "wwpt-52e3c-firebase-adminsdk-t78mc-622d420109.json")

# Initialize Firebase Admin SDK with the service account JSON file
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

# Initialize the OCR model
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # 'lang' can be changed if needed

# Define the path to the saved image
image_path = "wwpt.png"  # This is the image to be saved from the clipboard

# Define the path to store the username
username_file_path = "username.txt"

def get_username():
    """Function to get the username from a file or prompt the user if not available."""
    if os.path.exists(username_file_path):
        with open(username_file_path, 'r') as f:
            return f.read().strip()
    else:
        return None

def ask_for_username():
    """Prompt the user for a username, check its existence in Firestore, and save it."""
    while True:
        root = Tk()
        root.withdraw()  # Hide the main window
        username = simpledialog.askstring("Input", "Enter your username:", parent=root)
        root.destroy()

        if username:
            # Check if the username exists in Firestore
            user_ref = db.collection(username)  # Reference to the user's collection
            docs = user_ref.stream()

            if not list(docs):  # If no documents are found, the collection doesn't exist
                messagebox.showerror("Error", "Username doesn't exist.")
                continue  # Prompt for the username again
            else:
                # Username exists, save it locally
                with open(username_file_path, 'w') as f:
                    f.write(username)
                return username
        else:
            messagebox.showerror("Error", "Username cannot be empty.")

def edit_username():
    """Function to edit the username."""
    root = Tk()
    root.withdraw()  # Hide the main window
    username = simpledialog.askstring("Input", "Enter your new username:", parent=root)
    if username:
        with open(username_file_path, 'w') as f:
            f.write(username)
    root.destroy()

def quit_program(icon, item):
    """Function to quit the application."""
    icon.stop()
    os._exit(0)  # Ensure the program exits

def run_ocr():
    """Function to perform OCR on the saved image and save results to Firestore."""
    if not os.path.exists(image_path):
        print(f"Error: The file at {image_path} does not exist.")
    else:
        # Load the image
        image = cv2.imread(image_path)

        # Check if the image was loaded successfully
        if image is None:
            print(f"Error: Unable to load image at {image_path}. Please check the file path and integrity.")
        else:
            # Use PaddleOCR to read text from the full image (no cropping)
            result = ocr.ocr(image, cls=True)

            # Extract the number in ---/--- format from the result
            if result and result[0]:
                detected_text = result[0][0][1][0]  # Extracting detected text
                # Check if the text contains '/'
                if '/' in detected_text:
                    print(f"Detected 'plates' count: {detected_text}")

                    # Get the username
                    username = get_username()
                    if username:
                        # Check if the username collection exists in Firestore
                        user_ref = db.collection(username)
                        docs = user_ref.limit(1).get()  # Try to get at least one document from the collection

                        if not docs:
                            messagebox.showerror("Error", f"Username '{username}' does not exist in Firestore.")
                        else:
                            # If the username exists, save data
                            doc_ref = db.collection(username).document("save")
                            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            doc_ref.set({
                                "plate_number": detected_text,
                                "timestamp": current_time
                            })
                            print(f"Data saved to Firestore under '{username}' collection with document ID 'save'.")
                else:
                    messagebox.showerror("Error", "No valid 'plates' count found in the expected format.")
            else:
                messagebox.showerror("Error", "No text detected.")


def save_clipboard_image():
    """Function to save the current clipboard image as wwpt.png."""
    clipboard_image = ImageGrab.grabclipboard()

    if isinstance(clipboard_image, Image.Image):
        clipboard_image.save(image_path, "PNG")
        print(f"Image saved from clipboard as '{image_path}'.")
        run_ocr()  # Run OCR on the saved image
    else:
        messagebox.showerror("Error", "No image found in the clipboard.")

def show_settings_menu():
    """Function to show the settings window with options."""
    settings_window = tk.Tk()
    settings_window.title("Settings Menu")

    # Set the window size (e.g., 300x200 pixels)
    settings_window.geometry("300x100")  # Adjust width and height as needed

    # Button to edit username
    username_button = Button(settings_window, text="Edit Username", command=edit_username)
    username_button.pack(pady=10)

    # Button to generate image from clipboard and perform OCR
    generate_button = Button(settings_window, text="Generate", command=save_clipboard_image)
    generate_button.pack(pady=10)

    settings_window.mainloop()


def create_tray_icon():
    """Function to create the system tray icon."""
    icon_image = Image.open("icon.png")  # Replace with a path to your tray icon image

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
        username = ask_for_username()
        if username:
            show_settings_menu()
        else:
            print("No username provided. Exiting.")
            quit_program(None, None)
