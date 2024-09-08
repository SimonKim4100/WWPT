# WWPT(Wuthering Waves Plate Tracker)
Thank you for downloading WWPT! <br>
While I tried my best to make this program user-friendly, there were many limitations. Thus, I will write this README file that guides you step by step through all the programs that are required.

## Notice
1. This program DOES NOT access or alter any game files.
2. The database uses pseudo-authentication process, so please don't try to break through :)
3. **You do NOT need to press any of the Python scripts**

## Installation
### If you don't have Python(=if you are not a coder)
1. Download the `zip` files with versions, on the very right side of this Github screen. Unzip it to a safe location.
2. Install Python-3.10.11 that I have included. **Make sure to check "add Python to PATH"** in the very beginning of installation.
3. Run `install.bat`.
4. Run `wwpt.py` whenever you play the game. If you think this is too tedious, take a look at the `If you're lazy` section below.
### If you are a coder
1. Download the lastest release of WWPT
2. Create an environment with Python==3.10.11, and install requirements.txt 
```pip install -r requirements.txt```
3. Run `RUN.bat` whenever you play the game. If you think this is too tedious, take a look at the `If you're lazy` section below.<br>
4. Coders may need to change batch files by adding something like:<br>
`cd your_directory<br>
conda activate your_env`
<br>
**Warning**<br>
All batch files are NOT to be moved elsewhere. If you would like to move it, please make a shortcut file instead.

## Walkthrough
1. Launch `RUN.bat`. A window will ask for your username. This one, I will be distributing one for each one of you that contacts me. It won't ask anymore if you've properly entered your username the first time.
2. When the username is entered, the program will automatically be minimized into the Windows tray.
3. In-game, take a screenshot of your remaining plates with **Win+Shift+S**.
4. **Only screenshot the part where the plates are shown.**
5. Click on the tray --> right click on WWPT --> go to settings --> press "generate"
6. This will automaticall save your plates to the database.
7. Return to your mobile, and refresh! All done!<br>

## If you're lazy...
TL;DR: `Press batch_maker.bat`<br>
The python file(wwpt.py) has to be clicked everytime you launch your game. But having to run this file can be tedious, so I made an automated batch maker(batch_maker.bat). What this does, is it will ask for the directory of your game's launcher, and the wwpt.py file's directory. Entering them will make a "launch_game_and_wwpt.bat" which runs both the launcher and the python script at the same time.<br>
*So instead of pressing the launcher, from now on press this bat file.*<br>
Be wary that you must enter the **FILE'S DIRECTORY**, not the folder's directory. For example, the directory to my python file would be: <br>
`C:\\Users\\username\\Desktop\\GIT\\WWPT\\wwpt.py`<br>
and NOT<br>
`C:\\Users\\username\\Desktop\\GIT\\WWPT`<br>
Ignore the double slash, feel free to use single.

## APK file
https://drive.google.com/file/d/1K3sYktJogFG83XHWkSDR5ucGPRG4nT1F/view?usp=sharing <br>
Don't worry, it's hand made and safe XD<br>
<br>
Original Repo: https://github.com/SimonKim4100/WWPTm

