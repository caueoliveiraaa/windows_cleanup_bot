# NOTE - For more information, check the readme file

command_list = [
    # Recycle Bin
    r'del /s /q C:\$Recycle.Bin',
    # Temporary files
    r'del /q /f /s C:\Windows\Temp\*',
    # Prefetch Files
    r'del /q /f /s C:\Windows\Prefetch\*',
    # Windows Error Reporting
    r'del /q /f /s C:\ProgramData\Microsoft\Windows\WER\*',
    # Resolve DNS Issues
    'ipconfig /flushdns',
]
