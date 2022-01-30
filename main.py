import sys
from datetime import datetime


class CLI_colors():
    HDR = '\033[95m'  # header color
    OKB = '\033[94m'  # okay blue
    OKC = '\033[96m'  # okay cyan
    OKG = '\033[92m'  # okay green
    WARNING = '\033[31m'  # warning red
    CMT = '\033[93m'  # comment orange
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLR = '\033[0m'  # clear color

    def clear(self):
        print(self.CLR)


CLIC = CLI_colors()


def print_main_menu():
    print(f'{CLIC.OKB}Available commands:')
    print(f'{CLIC.CMT}"time" - {CLIC.CLR}print current time')
    print(f'{CLIC.CMT}"exit" - {CLIC.CLR}quit interface')
    CLIC.clear()


def main():
    program_status = True
    print(f'{CLIC.HDR}Welcome to TDS v0.1')
    print_main_menu()
    CLIC.clear()
    while program_status:
        print(f'{CLIC.CLR}Waiting for command...')
        command = input()
        if command == 'exit':
            program_status = False
        if command == 'time':
            print(datetime.now())

    print(f'{CLIC.OKG}Exiting program.{CLIC.CLR}')


if __name__ == "__main__":
    main()
