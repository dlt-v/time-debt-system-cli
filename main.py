import sys
import logging

from cli_commands import cli_cmds
from cli_colors import cli_colors

TDS = cli_cmds()
CLIC = cli_colors()


def main() -> None:
    program_status = True
    CLIC.clear()
    TDS.header()

    while program_status:
        try:
            print(
                f'{CLIC.CLR}Waiting for command... (Use "help" to see available commands.)')
            command_line = input('>').split()
            command = command_line[0]
            TDS.header()
            match command:
                case 'exit':
                    print(f'{CLIC.OKG}Exiting program with flag 0.{CLIC.CLR}')
                    program_status = False
                case 'time':
                    TDS.print_time()
                case 'help':
                    TDS.help()
                case 'add':
                    TDS.add_activity()
                case 'pom':

                    if(len(command_line) > 3):
                        try:
                            TDS.pomodoro(command_line[1], int(
                                command_line[2]), int(command_line[3]))
                        except TypeError:
                            print(
                                f'{CLIC.FAIL}ERROR: Invalid arguments{CLIC.CLR}')
                        except:
                            logging.exception(
                                f'{CLIC.FAIL}ERROR: Oops! Something went wrong...{CLIC.CLR}')

                    else:
                        TDS.pomodoro()
                case 'del':
                    TDS.delete_activity()
                case 'list':
                    if(len(command_line) > 1):
                        try:
                            TDS.list_activities(command_line[1])
                        except:
                            logging.exception(
                                f'{CLIC.FAIL}ERROR: Oops! Something went wrong...{CLIC.CLR}')
                    else:
                        TDS.list_activities()
                case 'wipe':
                    TDS.wipe()
                case _:
                    TDS.unknown_command()
        except KeyboardInterrupt:
            TDS.keyboard_interrupt()
            sys.exit()


if __name__ == "__main__":
    main()
