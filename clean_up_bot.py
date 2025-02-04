from command_list import command_list
import sys
import os


def display_error() -> None:
    exctp, exc, exctb = sys.exc_info()
    message = f'\ntraceback:{exctb.tb_frame.f_code.co_name}'
    message += f':{exctb.tb_lineno}:{exctp}:'
    print(('-' * 120) + f'\n{message}\n', end='')
    print(f'{exc}\n')


def main() -> None:
    print('Initiating cleaning process...')
    for command in command_list:
        print(('-' * 120) + f'\nExecuting command - {command}\n')
        try:
            os.system(command)
        except Exception:
            display_error()


if __name__ == '__main__':
    os.system('cls')
    main()
