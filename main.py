import sys

from cli_commands import cli_cmds
from cli_colors import cli_colors

TDS = cli_cmds()
CLIC = cli_colors()


def main():
    program_status = True
    TDS.header()
    CLIC.clear()
    while program_status:
        print(
            f'{CLIC.CLR}Waiting for command... (Use "help" to see available commands.)')
        command = input()
        if command == 'exit':
            print(f'{CLIC.OKG}Exiting program with flag 0.{CLIC.CLR}')
            program_status = False
        if command == 'time':
            TDS.print_time()
        if command == 'help':
            TDS.help()
        else:
            TDS.unknown_command()


if __name__ == "__main__":
    main()
