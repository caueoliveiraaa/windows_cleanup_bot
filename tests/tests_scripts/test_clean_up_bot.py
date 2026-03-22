"""Tests for cleanup Bot."""

from unittest import main

from test_base.base_test import BaseTestCase


class TestBot(BaseTestCase):
    """Tests for Bot functionalities."""

    def test_report_error_method(self) -> None:
        """Tests the show method of CliTerminal."""
        self.bot.show.side_effect = OSError("Error")
        self.bot.main()

        self.bot.bold.assert_called()
        self.bot.underline.assert_called()
        self.bot.report_error.assert_called()


if __name__ == "__main__":
    main()
