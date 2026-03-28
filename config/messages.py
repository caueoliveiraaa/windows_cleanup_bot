"""Stores messages printed by the bot.

Constants
---------

EXECUTING (dict[str, str]): Execution of the command.
OUTPUT (dict[str, str]): Output of the command.
SUCCESS (dict[str, str]): Success message for end of execution.
"""

EXECUTING: dict[str, str] = {
    "message": f"{('-'*100)}\nExecuting command:", 
    "color": "blue", 
    "end": " ",
}
OUTPUT: dict[str, str] = {
    "message": "Output", 
    "color": "blue", 
    "end" :"\n\n",
}
SUCCESS: dict[str, str] = {
    "message": (
        f"{('-'*100)}"
        "\nAll commands executed successfully!\n"    
        f"{('-'*100)}"
    ),
    "color": "green", 
    "end": "\n",
}
