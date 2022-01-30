import sys

from cli_commands import cli_cmds
from cli_colors import cli_colors

TDS = cli_cmds()
CLIC = cli_colors()


def main():
    program_status = True
    CLIC.clear()
    while program_status:

        print(
            f'{CLIC.CLR}Waiting for command... (Use "help" to see available commands.)')
        command = input()
        TDS.header()
        match command:
            case 'exit':
                print(f'{CLIC.OKG}Exiting program with flag 0.{CLIC.CLR}')
                program_status = False
            case 'time':
                TDS.print_time()
            case 'help':
                TDS.help()
            case _:
                TDS.unknown_command()


if __name__ == "__main__":
    main()
