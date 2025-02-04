import sys
import os


def display_error() -> None:
    """ Show error message. """

    exctp, exc, exctb = sys.exc_info()
    message = f'\ntraceback:{exctb.tb_frame.f_code.co_name}'
    message += f':{exctb.tb_lineno}:{exctp}:'
    print(message, end='')
    print(f'{exc}\n')


def main() -> None:
    """ Clean up junk files and others. """

    # NOTE: Add commands and paths here
    commandList = [
        'del /q /f /s %temp%\*',
        'ipconfig /flushdns',
    ]

    for command in commandList:
        print('-'*120)
        print(f'Executing command: {command}:\n')
        try:
            os.system(command)
        except Exception:
            display_error()


if __name__ == '__main__':
    os.system('cls')
    main()
