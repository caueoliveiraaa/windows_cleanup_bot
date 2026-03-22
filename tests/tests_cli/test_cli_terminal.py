"""Tests for CLI terminal."""

from unittest import main

from test_base.base_test import BaseTestCase


class TestCLITerminal(BaseTestCase):
    """Tests for CLI terminal functionalities."""

    def test_show_method(self) -> None:
        """Tests the show method of CliTerminal."""
        test_message = "Hello, World!"
        self.terminal.show(message=test_message, color="green", end="\n")

        self.terminal.show.assert_called_with(
            message=test_message, color="green", end="\n"
        )

    def test_underline_method(self) -> None:
        """Tests the underline method of CliTerminal."""
        test_message = "Hello, World!"
        self.terminal.underline(message=test_message, color="green", end="\n")

        self.terminal.underline.assert_called_with(
            message=test_message, color="green", end="\n"
        )

    def test_bold_method(self) -> None:
        """Tests the bold method of CliTerminal."""
        test_message = "Hello, World!"
        self.terminal.bold(message=test_message, color="green", end="\n")

        self.terminal.bold.assert_called_with(
            message=test_message, color="green", end="\n"
        )


if __name__ == "__main__":
    main()
