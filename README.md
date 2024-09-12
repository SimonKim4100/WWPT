# WWPT(Wuthering Waves Plate Tracker)
[한국어](README.kr.md)<br>
Thank you for downloading WWPT! <br>
While I tried my best to make this program user-friendly, there were many limitations. Thus, I will write this README file that guides you step by step through all the programs that are required.

## Notice
1. This program DOES NOT access or alter any game files.
2. The database uses pseudo-authentication process, so please don't try to break through :)
3. **Please download the releases and NOT the repository**

**Warning**<br>
All batch files are NOT to be moved elsewhere. If you would like to move it, please make a shortcut file instead.

## Walkthrough
1. Launch `wwpt.exe`. A window will ask for your username. This one, I will be distributing one for each one of you that contacts me. It won't ask anymore if you've properly entered your username the first time.
2. When the username is entered, the program will automatically be minimized into the Windows tray. Launches afterward will automaticall store program in tray.
3. Click on tray --> right click on WWPT --> go to settings --> enter plates and save
4. This will automaticall save your plates to the database.
5. Return to your mobile, and refresh! All done!<br>

## If you're lazy...
TL;DR: `Press batch_maker.bat`<br>
The exe has to be clicked everytime you launch your game. But having to run this everytime can be tedious, so I made an automated batch maker(batch_maker.bat). What this does, is it will ask for the directory of your game's launcher, and exe's directory. Entering them will make a "launch_game_and_wwpt.bat" which runs both the launcher and the python script at the same time.<br>
*So instead of pressing the launcher, from now on press this bat file.*<br>
Be wary that you must enter the **FILE'S DIRECTORY**, not the folder's directory. For example, the directory to my python file would be: <br>
`C:\\Users\\username\\Desktop\\GIT\\WWPT\\wwpt.py`<br>
and NOT<br>
`C:\\Users\\username\\Desktop\\GIT\\WWPT`<br>
Ignore the double slash, feel free to use single.

## APK file
https://drive.google.com/file/d/1Jq4byWekpWzGP7RU30qs3QywwDogkJIa/view?usp=sharing <br>
Don't worry, it's hand made and safe XD<br>
<br>
Original Repo: https://github.com/SimonKim4100/WWPTm

## Others
EXE build with Nuitka
Scripts built with Python==3.10
Username dataset is saved in registry, please contact me if you are concerned.
