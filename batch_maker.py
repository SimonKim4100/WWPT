import os

def create_batch(game_dir, python_script_dir):
    # Batch file content
    batch_content = f'''@echo off
start "" "{game_dir}"
start "" "python" "{python_script_dir}"
'''

    # Path to save the batch file
    batch_file_path = os.path.join(os.getcwd(), 'launch_game_and_wwpt.bat')

    # Write the batch content to the file
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(batch_content)

    print(f"Batch file created at: {batch_file_path}")
    print("You can double-click this batch file to run both the game and wwpt.py.")


def main():
    # Ask for the game executable directory
    game_dir = input("Enter the full path to the game executable (e.g., D:\\Wuthering Waves\\launcher.exe): ").strip()
    
    # Validate if the input is correct
    while not os.path.isfile(game_dir):
        print(f"The file '{game_dir}' does not exist. Please enter a valid path.")
        game_dir = input("Enter the full path to the game executable: ").strip()

    # Ask for the wwpt.py directory
    python_script_dir = input("Enter the full path to RUN.bat (e.g., C:\\Users\\username\\Desktop\\GIT\\WWPT\\wwpt.py): ").strip()
    
    # Validate if the input is correct
    while not os.path.isfile(python_script_dir):
        print(f"The file '{python_script_dir}' does not exist. Please enter a valid path.")
        python_script_dir = input("Enter the full path to wwpt.py: ").strip()

    # Create the batch file
    create_batch(game_dir, python_script_dir)


if __name__ == "__main__":
    main()
