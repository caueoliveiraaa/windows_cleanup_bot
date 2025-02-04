## About This Python Script:

- This project is a `Python` script that cleans up junk files and folders in your `Windows` system to make space for more important things.
- It executes `commands` via terminal to clean up as much space as possible and it's customizable for you to add more `commands`.
- The code was written in `Python`, version `3.12.1`.
- This script was created to run on `Windows`. The necessary ajustments would have to be made for `Linux` distributions.
- If you have changed paths such as `C:\$Recycle.Bin` or `C:\Windows\Temp\`, this will affact this script.

## Using This Script:

- **Python**: Download [Python](https://www.python.org/downloads/), make sure it's installed, working, and on a version higher or equal to `3.12.1`.
- **Add more commands**: For more paths, folders, and files to be deleted, add the necessary commands to the `command_list.py` file.
- **Running the script**: All we have to do is enter the main directory of the project, and run the script once `Python` is already installed.

## The Delete Command:

- **del**: This is the command used to `delete` files in the Command Prompt (cmd) on Windows.
- **/q**: This switch stands for `quiet mode`. It suppresses the confirmation prompt that usually appears when deleting files
- **/f**: This switch stands for `force`. It forces the deletion of read-only files.
- **/s**: This switch stands for `subdirectories.` It tells the command to delete files in all subdirectories of the specified directory

## The `ipconfig /flushdns` Command:

- **ipconfig**: This is a command-line utility that displays all current TCP/IP network configuration values and refreshes DHCP and DNS settings.
- **/flushdns**: This switch tells ipconfig to flush the DNS resolver cache. Flushing the DNS cache removes all entries and forces the computer to repopulate those addresses the next time they are needed.
- **Resolve DNS Issues**: If you're experiencing issues with DNS resolution, such as being unable to access certain websites, flushing the DNS cache can help resolve these issues.
- **Update DNS Records**: If DNS records have changed (e.g., a website has moved to a new server), flushing the DNS cache ensures that your computer uses the updated DNS information.