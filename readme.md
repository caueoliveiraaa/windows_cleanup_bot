## About The Script:

- This project is a Python script that cleans up junk files and folders in your windows system.
- It executes commands via terminal to clean up as much space as possible.
- The Python code was written in Python version 3.12.1.
- This script was created to run on Windows. The necessary ajustments would have to be made for Linux distributions.

## Using The Script:

- **Python**: Download [Python](https://www.python.org/downloads/), make sure it's installed, working, and on a version higher or equal to `3.12.1`.
- **Add more commands**: For more paths, folders, and files to be deleted, add the necessary commands to the `command_list.py` file.

## The Delete Command:

- **del**: This is the command used to `delete` files in the Command Prompt (cmd) on Windows.
- **/q**: This switch stands for `quiet mode`. It suppresses the confirmation prompt that usually appears when deleting files
- **/f**: This switch stands for `force`. It forces the deletion of read-only files.
- **/s**: This switch stands for `subdirectories.` It tells the command to delete files in all subdirectories of the specified directory