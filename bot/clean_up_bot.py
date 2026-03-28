"""This bot is responsible for cleaning up space in a windows OS."""

from os import system

from beartype import beartype
from rich.console import Console

from config.command_list import COMMAND_LIST
from config.messages import EXECUTING, OUTPUT, SUCCESS


class Bot():
    """Bot class responsible for executing the cleanup commands."""

    def __init__(self, console: Console) -> None:
        """Initializes the Bot class.
        
        Parameters
        ----------
        console : Console
            Class Console from the rich lib for printing.

        Attributes
        ----------
        self._console : Console
            Instance of the rich console for printing.
        """
        self._console: Console = console()

    @beartype
    def show(self, message: str, color: str, end: str) -> None:
        """Prints a message to the terminal using rich formatting.

        Parameters
        ----------
        message : str
            The message to be printed.
        color : str
            The color of the message text.
        end : str
            The break of the line.
        """
        self._console.print(f"[{color}]{message}[/{color}]", end=end)

    @beartype
    def main(self) -> None:
        """Executes the bot and all the commands."""
        for command in COMMAND_LIST:
            self.show(**EXECUTING)
            self.show(f"{command}\n", "green", "\n")
            self.show(**OUTPUT)
            system(command)
        self.show(**SUCCESS)
