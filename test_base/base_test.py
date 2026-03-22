"""File responsible for creating the base test class."""

import io
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from beartype.typing import Any, Dict, Optional

from bot.clean_up_bot import Bot
from cli.rich_terminal import CliTerminal


class BaseTestCase(TestCase):
    """
    Base test class that sets up standard methods that can be imported
    by test classes to use the same methods.

    Thus, by simply importing the BaseTestCase, the "setUpClass"
    and "tearDownClass" methods below will be executed automatically, and elements
    like 'sleep' and 'print' will not affect the tests.
    """

    _mocks: Dict[str, Optional[Any]] = {}
    _patchers: Dict[str, Any] = {}
    _original_stderr: Any = None

    def setUp(self) -> None:
        """Sets up the test environment."""
        super().setUp()
        self.terminal: CliTerminal = MagicMock(spec=CliTerminal)
        self.bot: Bot = MagicMock(spec=Bot)

    @classmethod
    def setUpClass(cls) -> None:
        """
        Overrides methods that can influence tests when executing them.
        More methods to be overridden can be added here.

        Args:
            cls: It is a convention (like self), short for 'class'
        """
        cls._patchers = {
            "print": patch("builtins.print", return_value=None),
            "traceback": patch("traceback.print_exception", return_value=None),
            "sleep": patch("time.sleep", return_value=None),
            "logger": patch("logging.Logger._log", return_value=None),
        }

        cls._mocks = {name: patcher.start() for name, patcher in cls._patchers.items()}

        cls._original_stderr = sys.stderr
        sys.stderr = io.StringIO()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Ends the methods that were overwritten at the end of the tests.
        More methods to be overridden can be added here.

        Args:
            cls: It is a convention (like self), short for 'class'
        """
        for patcher in cls._patchers.values():
            patcher.stop()

        sys.stderr = cls._original_stderr
