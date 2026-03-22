"""This bot is responsible for cleaning up space in the computer."""

import os
import sys

from cli.rich_terminal import CliTerminal
from data.command_list import COMMAND_LIST


class Bot(CliTerminal):
    """Bot class responsible for executing the cleanup commands."""

    def report_error(self) -> None:
        """Displays the error information."""
        exctp, exc, exctb = sys.exc_info()

        message: str = f"\ntraceback:{exctb.tb_frame.f_code.co_name}"
        message += f":{exctb.tb_lineno}:{exctp}:"

        self.underline(("-" * 120) + f"\n{message}\n", color="red")
        self.bold(f"{exc}\n", color="red")

    def main(self) -> None:
        """Executes the bot."""
        for command in COMMAND_LIST:
            try:
                self.show(
                    message=f"{('-'*200)}\nExecuting command:", color="blue", end=" "
                )
                self.show(message=f"{command}\n", color="green")
                self.show(message="Output:", color="blue", end="\n\n")

                os.system(command)

            except OSError:
                self.report_error()
            except ValueError:
                self.report_error()

        self.show(
            message=f"{('-'*200)}\nAll commands executed successfully!\n{('-'*200)}",
            color="green",
        )


if __name__ == "__main__":
    print("This module is intended to be imported and used in other scripts.")
