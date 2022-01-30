from datetime import datetime
import os

from cli_colors import cli_colors

CLIC = cli_colors()


class cli_cmds():
    _current_balance = 0

    def header(self):
        self.__cls()
        print(f'{CLIC.HDR}TDS_CLI v0.1{CLIC.CLR}')
        print(
            f'Current balance is: {self.print_balance()}{CLIC.CLR}.\n')

    def print_balance(self):
        if self._current_balance == 0:
            return f'{CLIC.CMT}0'
        elif self._current_balance < 0:
            return f'{CLIC.WRN}{self._current_balance}'
        elif self._current_balance > 0:
            return f'{CLIC.OKG}{self._current_balance}'

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

    def unknown_command(self):
        print(
            f'{CLIC.WRN}ERROR: Unknown command.{CLIC.CLR}')

    def __cls(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
