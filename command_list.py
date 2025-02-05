# Add extra commands to be executed by the script in the command_list.
# NOTE: For more information, check the readme.md file.

delete_command = 'del /q /f /s '
disk_cleanup_command = 'cleanmgr'
dns_cleanup_command = 'ipconfig /flushdns'

command_list = [
    delete_command + r'C:\$Recycle.Bin',
    delete_command + r'C:\Windows\Temp\*',
    delete_command + r'%temp%\*',
    delete_command + r'C:\Windows\Prefetch\*',
    delete_command + r'C:\ProgramData\Microsoft\Windows\WER\*',
    dns_cleanup_command,
    # disk_cleanup_command,  # This will open the Disk Cleanup utility
]
