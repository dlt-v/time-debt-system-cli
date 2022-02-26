from datetime import datetime
from typing import List
from time import sleep  # for pomodoro
# from playsound import playsound
import runtime_types
import os

from cli_colors import cli_colors
from activity_tracker import Tracker

CLIC = cli_colors()
activity_tracker = Tracker()


class cli_cmds():
    _current_balance = activity_tracker.return_balance()
    _weights = {
        'university': 1,
        'programming': 1,
        'reading': .5,
        'hobby': .5,
    }

    def header(self) -> None:
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

    def print_time(self) -> None:
        now = datetime.now()
        print(f'{CLIC.CMT}It\'s {now.hour}:{now.minute}.')
        CLIC.clear()

    def add_activity(self) -> None:
        new_activity: runtime_types.NewActivity = {
            'name': '',
            'length': 0,
            'weight': 0
        }
        data = self.__choose_category()
        if len(data[0]) == 0 or len(data[1]) == 0:
            print(f'{CLIC.WRN}ERROR: Unexpected value.{CLIC.CLR}')
            return

        new_activity['name'] = data[0]
        new_activity['weight'] = float(data[1])

        print(f'{CLIC.CMT} Length (in hours): {CLIC.CLR}')
        length = float(input('>'))
        new_activity['length'] = length
        activity_tracker.add_activity(new_activity)
        self._current_balance = activity_tracker.return_balance()

    def pomodoro(self, name: str = '', category: int = -1, length: int = -1) -> None:
        new_activity: runtime_types.NewActivity = {
            'name': '',
            'length': 0,
            'weight': 0
        }

        if(len(name) == 0):
            data = self.__choose_category()
            if len(data[0]) == 0 or len(data[1]) == 0:
                print(f'{CLIC.WRN}ERROR: Unexpected value.{CLIC.CLR}')
                return

            new_activity['name'] = data[0]
            new_activity['weight'] = float(data[1])

            print(f'{CLIC.CMT}Enter length of the pomodoro (in minutes):{CLIC.CLR}')
            time: int = int(input('>'))
        else:
            new_activity['name'] = name
            new_activity['weight'] = float(category)
            time = length

        current_time = 0
        header = f'Activity:{CLIC.OKC} {new_activity["name"]}{CLIC.CLR}'
        command_line_width = max(18, len(header))
        os.system(f'mode con: cols={command_line_width} lines=5')

        while current_time <= (time * 60):

            print(f'{CLIC.HDR}TDS POMIDORO{CLIC.CLR}')
            print(header)

            time_passed = f'{activity_tracker.format_time(current_time // 60)}:{activity_tracker.format_time(current_time % 60)}'
            print(f'Time passed: {CLIC.OKC}{time_passed}{CLIC.CLR}')

            time_left = f'{activity_tracker.format_time((time * 60 - current_time) // 60)}:{activity_tracker.format_time((time * 60 - current_time) % 60)}'
            print(f'Time left: {CLIC.OKC}{time_left}{CLIC.CLR}')

            sleep(1)
            current_time += 1
            self.__cls()

        os.system('mode con: cols=80 lines=15')
        # TODO: playsound.playsound('bell.wav')
        print(f'{CLIC.OKG}Pomodoro finished!{CLIC.CLR}')
        print(
            f'{CLIC.CMT}Activity \"{new_activity["name"]}\" added to activity list.{CLIC.CLR}')
        new_activity['length'] = round(time / 60, 2)
        activity_tracker.add_activity(new_activity)
        self._current_balance = activity_tracker.return_balance()

    def delete_activity(self) -> None:
        print(f'{CLIC.CMT} ID of the item you want to delete: {CLIC.CLR}')
        id: int = int(input('>'))
        if type(id) is int:
            activity_tracker.delete_activity(id)
        else:
            print('')
            print(f'{CLIC.WRN}ERROR: Invalid input{CLIC.CLR}')

    def list_activities(self) -> None:
        activity_tracker.list_activities()

    def wipe(self) -> None:
        activity_tracker.wipe()

    def help(self) -> None:
        # prints all the available commands to the console.
        print(f'{CLIC.OKB}Available commands:')
        print(f'{CLIC.CMT}"add"{CLIC.CLR} - add activity')
        print(f'{CLIC.CMT}"pom"{CLIC.CLR} - start a pomodoro session {CLIC.OKC}(f_cmd name category minutes){CLIC.CLR}')
        print(f'{CLIC.CMT}"del"{CLIC.CLR} - delete activity')
        print(f'{CLIC.CMT}"list"{CLIC.CLR} - list registered activities')
        print(f'{CLIC.CMT}"time"{CLIC.CLR} - print current time')
        print(f'{CLIC.CMT}"help"{CLIC.CLR} - view available commands')
        print(f'{CLIC.CMT}"wipe"{CLIC.CLR} - delete every activity')
        print(f'{CLIC.CMT}"exit"{CLIC.CLR} - quit interface')
        CLIC.clear()

    def unknown_command(self) -> None:
        print(
            f'{CLIC.WRN}ERROR: Unknown command.{CLIC.CLR}')

    def keyboard_interrupt(self) -> None:
        print(f'{CLIC.WRN}ERROR: Unexpected interrupt.{CLIC.CLR}')
        print(f'{CLIC.CMT}Exiting program with flag 1.{CLIC.CLR}')

    def __cls(self) -> None:
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def __choose_category(self) -> List[str]:
        print(f'{CLIC.CMT} Name / Comment: {CLIC.CLR}')
        name = input('>')

        print(f'{CLIC.CMT} Category of output activity: {CLIC.CLR}')
        for i, key in enumerate(self._weights):
            print(f'{i} - {key}')
        print(f'{len(self._weights.keys()) + 1} - custom')

        choice = int(input('>'))
        if choice in range(len(self._weights)):
            list_of_keys = list(self._weights.keys())
            weight = str(self._weights[list_of_keys[choice]])
        elif choice == (len(self._weights.keys()) + 1):
            print(f'{CLIC.CMT} Add custom weight (float value): {CLIC.CLR}')
            weight = input('>')
        else:
            return ['', '']
        print([name, weight])
        return [name, weight]
