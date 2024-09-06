@echo off
:: Set the current directory where the batch file and wwpt.py are located
set "script_dir=%~dp0"

:: Set the path to the Python executable (relative to the current directory)
set "python_exe=%script_dir%Python\python.exe"

:: Run the Python script using the Python executable
"%python_exe%" "%script_dir%batch_maker.py"
