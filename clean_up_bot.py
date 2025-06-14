""" This bot is responsable for cleaning up space in the computer """
import os
import sys
from command_list import command_list


def display_error() -> None:
    """ Displays the error information """
    exctp, exc, exctb = sys.exc_info()
    message = f'\ntraceback:{exctb.tb_frame.f_code.co_name}'
    message += f':{exctb.tb_lineno}:{exctp}:'
    print(('-' * 120) + f'\n{message}\n', end='')
    print(f'{exc}\n')


def main() -> None:
    """ Executes the bot """
    for command in command_list:
        print(('-' * 120) + f'\nExecuting command: {command}\n')
        try:
            os.system(command)
        except Exception as erro:
            display_error()
            raise erro


if __name__ == '__main__':
    os.system('cls')
    main()
