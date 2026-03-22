"""Entry point of the project."""

from os import system

from bot.clean_up_bot import Bot


def main() -> None:
    """Executes the cleaning bot."""
    system("cls")
    bot: Bot = Bot()
    bot.main()


if __name__ == "__main__":
    main()
