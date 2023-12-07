import sys
import os


def display_error() -> None:
    """ Show error message. """

    red = '\033[031m'
    yellow = '\033[033m'
    close = '\033[0m'
    exctp, exc, exctb = sys.exc_info()
    message = f'\ntraceback:{exctb.tb_frame.f_code.co_name}:{exctb.tb_lineno}:{exctp}:'
    message_error += f'{exc}\n'
    print(yellow + message + close, end='')
    print(red + message_error + close)


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
        except:
            display_error()


if __name__ == '__main__':
    os.system('cls')
    main()
