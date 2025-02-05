## About This Project:

- **Purpose**: This project is a `Python` script designed to clean up junk files and folders on your `Windows` system, freeing up space for more important data. 
- **Platform**: The script is specifically designed for `Windows`. Adjustments would be required for compatibility with `Linux` distributions.
- **Method**: The script executes commands via the terminal to maximize space cleanup and is customizable, allowing you to add additional commands as needed.
- **Windows Paths**: If you have modified default paths such as `C:\$Recycle.Bin` or `C:\Windows\Temp\`, these changes will affect the script's functionality.
- **Python Version**: The script is written in `Python`, version `3.12.1`.

## About The Python Script:

- **Download Python**: Ensure [Python](https://www.python.org/downloads/) is installed and working on your system, with a version higher or equal to `3.12.1.1`.
- **Add Commands**: To delete additional paths, folders, and files, add the necessary commands to the `command_list.py` file.
- **Run The Script**: Navigate to the main directory of the project and run the script once `Python` is installed and set up.
- **Disk Cleanup**: If the `cleanmgr` command is included in the `command_list`, it will open a window to configure the cleaning process.

## The Delete Command:

- **del**: This is the command used to `delete` files in the Command Prompt (cmd) on `Windows`.
- **/q**: This switch stands for `quiet mode`. It suppresses the confirmation prompt that usually appears when deleting files.
- **/f**: This switch stands for `force`. It forces the deletion of read-only files.
- **/s**: This switch stands for `subdirectories.` It tells the command to delete files in all subdirectories of the specified directory.

## The ipconfig /flushdns Command:

- **ipconfig**: This is a command-line utility that displays all current `TCP/IP` network configuration values and refreshes `DHCP` and `DNS` settings.
- **/flushdns**: This switch tells ipconfig to flush the `DNS` resolver cache. Flushing the `DNS` cache removes all entries and forces the computer to repopulate those addresses the next time they are needed.
- **Resolve DNS Issues**: If you're experiencing issues with `DNS` resolution, such as being unable to access certain websites, flushing the `DNS` cache can help resolve these issues.
- **Update DNS Records**: If `DNS` records have changed (e.g., a website has moved to a new server), flushing the `DNS` cache ensures that your computer uses the updated `DNS` information.

## Manual Options:

- **Storage Sense**: https://support.microsoft.com/en-us/windows/manage-drive-space-with-storage-sense-654f6ada-7bfc-45e5-966b-e24aded96ad5
- **Cleanup recommendations**: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32

## Information Sources:

- **Free up drive space**: https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32
- **How to Delete Temporary Files**: https://www.supportyourtech.com/articles/how-to-delete-temporary-files-in-windows-10-using-cmd-a-step-by-step-guide/