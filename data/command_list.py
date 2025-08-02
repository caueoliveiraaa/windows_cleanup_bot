"""
Add extra commands to be executed by the script in the command_list.
NOTE: For more information, check the readme.md file.
"""

DELETE = 'del /q /f /s '
DISK_CLEANUP = 'cleanmgr'
DNS_CLEANUP = 'ipconfig /flushdns'

command_list = [
    DELETE + r'C:\$Recycle.Bin',
    DELETE + r'C:\Windows\Temp\*',
    DELETE + r'%temp%\*',
    DELETE + r'C:\Windows\Prefetch\*',
    DELETE + r'C:\ProgramData\Microsoft\Windows\WER\*',
    DNS_CLEANUP,
    DISK_CLEANUP,
]
