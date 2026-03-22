"""Add extra commands to be executed by the script in the command_list."""

from beartype.typing import List

DELETE_COMMAND: str = "del /q /f /s "
DISK_CLEANUP_COMMAND: str = "cleanmgr"
DNS_CLEANUP_COMMAND: str = "ipconfig /flushdns"

COMMAND_LIST: List[str] = [
    DELETE_COMMAND + r"C:\$Recycle.Bin",
    DELETE_COMMAND + r"C:\Windows\Temp\*",
    DELETE_COMMAND + r"%temp%\*",
    DELETE_COMMAND + r"C:\Windows\Prefetch\*",
    DELETE_COMMAND + r"C:\ProgramData\Microsoft\Windows\WER\*",
    DELETE_COMMAND + r"C:\ProgramData\Adobe\Common\Media Cache Files",
    DELETE_COMMAND + r"C:\Users\*\AppData\Local\pip\cache",
    DELETE_COMMAND + r"C:\Users\*\AppData\Local\npm-cache",
    DELETE_COMMAND + r"C:\Users\*\.npm",
    DELETE_COMMAND + r"C:\Users\*\AppData\Local\Google\Chrome\User Data\Default\Cache",
    DELETE_COMMAND + r"%appdata%",
    DNS_CLEANUP_COMMAND,
    DISK_CLEANUP_COMMAND,
]
