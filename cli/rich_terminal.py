"""This module provides rich terminal functionalities for the CLI."""

from rich.console import Console


class CliTerminal:
    """Class for rich terminal functionalities."""

    def __init__(self):
        """Initializes the CliTerminal class."""
        self._console: Console = Console()

    def show(self, message: str, color: str = "white", end: str = "\n") -> None:
        """
        Prints a message to the terminal using rich formatting.

        Args:
            message (str): The message to be printed.
            color (str): The color of the message text.
            end (str): The end character after the message.
        """
        self._console.print(f"[{color}]{message}[/{color}]", end=end)

    def underline(self, message: str, color: str = "white") -> None:
        """
        Prints an underlined message to the terminal using rich formatting.

        Args:
            message (str): The message to be printed.
            color (str): The color of the message text.
        """
        self._console.print(f"[underline {color}]{message}[/{color}]")

    def bold(self, message: str, color: str = "white", end: str = "\n") -> None:
        """
        Prints a bold message to the terminal using rich formatting.

        Args:
            message (str): The message to be printed.
            color (str): The color of the message text.
            end (str): The end character after the message.
        """
        self._console.print(f"[bold {color}]{message}[/{color}]", end=end)


if __name__ == "__main__":
    print("This module is intended to be imported and used in other scripts.")
