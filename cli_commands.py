from datetime import datetime
import os

from cli_colors import cli_colors
from activity_tracker import Tracker

CLIC = cli_colors()
activity_tracker = Tracker()


class cli_cmds():
    _current_balance = activity_tracker.return_balance()

    def header(self):
        self.__cls()
        print(f'{CLIC.HDR}TDS_CLI v0.1{CLIC.CLR}')
        print(
            f'Current balance: {self.print_balance()}{CLIC.CLR}.\n')

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

    def add_activity(self):
        new_activity = {}
        print(f'{CLIC.CMT} Name / Comment: {CLIC.CLR}')
        name = input('>')
        new_activity.update({'name': name})

        print(f'{CLIC.CMT} Category of output activity: {CLIC.CLR}')
        print(f'1 - University')
        print(f'2 - Hobby programming')
        print(f'3 - Maintenance/Chores')
        print(f'4 - Reading')
        category = int(input('>'))
        match category:
            case 1:
                new_activity.update({'weight': 0.5})
            case 2:
                new_activity.update({'weight': 0.25})
            case 3:
                new_activity.update({'weight': 0.25})
            case 4:
                new_activity.update({'weight': 0.25})
            case _:
                print(f'{CLIC.WRN}ERROR: Unexpected value.{CLIC.CLR}')
                return

        print(f'{CLIC.CMT} Length (in hours): {CLIC.CLR}')
        length = float(input('>'))
        new_activity.update({'length': length})
        activity_tracker.add_activity(new_activity)
        self._current_balance = activity_tracker.return_balance()

    def delete_activity(self):
        print(f'{CLIC.CMT} ID of the item you want to delete: {CLIC.CLR}')
        id = int(input('>'))
        if type(id) is int:
            activity_tracker.delete_activity(id)
        else:
            print('')
            print(f'{CLIC.WRN}ERROR: Invalid input{CLIC.CLR}')

    def list_activities(self):
        activity_tracker.list_activities()

    def help(self):

        print(f'{CLIC.OKB}Available commands:')
        print(f'{CLIC.CMT}"add"{CLIC.CLR} - add activity')
        print(f'{CLIC.CMT}"del"{CLIC.CLR} - delete activity')
        print(f'{CLIC.CMT}"list"{CLIC.CLR} - list registered activities')
        print(f'{CLIC.CMT}"time"{CLIC.CLR} - print current time')
        print(f'{CLIC.CMT}"help"{CLIC.CLR} - view available commands')
        print(f'{CLIC.CMT}"exit"{CLIC.CLR} - quit interface')
        CLIC.clear()

    def unknown_command(self):
        print(
            f'{CLIC.WRN}ERROR: Unknown command.{CLIC.CLR}')

    def keyboard_interrupt(self):
        print(f'{CLIC.WRN}ERROR: Unexpected interrupt.{CLIC.CLR}')
        print(f'{CLIC.CMT}Exiting program with flag 1.{CLIC.CLR}')

    def __cls(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
