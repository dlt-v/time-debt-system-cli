from datetime import datetime
import os

from cli_colors import cli_colors

CLIC = cli_colors()


class cli_cmds():

    def print_time(self):
        now = datetime.now()
        print(f'{CLIC.CMT}It\'s {now.hour}:{now.minute}.')
        CLIC.clear()

    def help(self):

        print(f'{CLIC.OKB}Available commands:')
        print(f'{CLIC.CMT}"time"{CLIC.CLR} - print current time')
        print(f'{CLIC.CMT}"help"{CLIC.CLR} - view available commands')
        print(f'{CLIC.CMT}"exit"{CLIC.CLR} - quit interface')
        CLIC.clear()

    def header(self):
        self.__cls()
        print(f'{CLIC.HDR}Welcome to TDS v0.1{CLIC.CLR}\n')

    def unknown_command(self):
        print(
            f'{CLIC.WRN}ERROR: Unknown command.{CLIC.CLR}')

    def __cls(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
