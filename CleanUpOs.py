import sys
import os


def display_error() -> None:
    """ Show error message. """

    exctp, exc, exctb = sys.exc_info()
    message = f'\ntraceback:{exctb.tb_frame.f_code.co_name}:{exctb.tb_lineno}:{exctp}:'
    message_error += f'{exc}\n'
    print('\033[33m' + message + '\033[0m', end='')
    print('"\033[33m' + message_error + '\033[0m"')


def main() -> None:
    """ Clean up junk files and others. """

    # NOTE: Add commands and paths here
    commandList = [
        'del /q /f /s %temp%\*',
        'del /q /f /s %appdata%\*',
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
