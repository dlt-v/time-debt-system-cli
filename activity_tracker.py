import json
import runtime_types
from typing import List
import datetime
from cli_colors import cli_colors

CLIC = cli_colors()


class Tracker():
    _next_id: int = 0
    _activity_list: List[runtime_types.Activity] = []

    def __init__(self) -> None:
        self.__update_from_json()

    def add_activity(self, activity: runtime_types.NewActivity) -> None:

        new_activity: runtime_types.Activity = {
            'id': self._next_id,
            'name': activity['name'],
            'weight': activity['weight'],
            'length': activity['length'],
            # hour/minutes/day of the week/day-month/month/year
            'time_added': datetime.datetime.now().strftime("%H/%M/%w/%d/%m/%Y")
        }
        self._next_id += 1
        self._activity_list.append(new_activity)
        self.__write_json()

    def list_activities(self, list_all: bool = False) -> None:

        print(
            f"ID\tLength\tTime added\tName\n")
        
        current_day: str = datetime.datetime.now().strftime("%d/%m/%Y")

        for activity in self._activity_list[::-1]:
            if (not list_all and activity['time_added'][8:] != current_day):
                break
            activity_time: datetime.datetime = datetime.datetime.strptime(
                activity['time_added'], "%H/%M/%w/%d/%m/%Y")

            delta: datetime.timedelta = datetime.datetime.now() - activity_time

            time_stamp: str = ''

            if delta.days == 0:
                time_stamp = f'{self.format_time(activity_time.hour)}:{self.format_time(activity_time.minute)}\t'
            elif delta.days == 1:
                time_stamp = 'yesterday'
            elif delta.days < 7:
                time_stamp = activity_time.strftime('%A')
            else:
                time_stamp = activity_time.strftime('%d.%m.%Y')

            print(
                f"{activity['id']}.\t{activity['length']}\t{time_stamp}\t{activity['name'][0:15]}{ '...' if len(activity['name']) > 15 else ''}")

        print("\n")

    def delete_activity(self, id: int) -> None:
        for i, activity in enumerate(self._activity_list):
            if activity["id"] == id:
                print('Are you sure you want to delete this item? y/n')
                choice = input(">").lower()
                match choice:
                    case 'y':
                        del self._activity_list[i]
                        self.__write_json()
                        return
                    case 'n':
                        print(f'{CLIC.WRN}Aborting...{CLIC.CLR}')
                        return
                    case _:
                        print(f'{CLIC.WRN}ERROR: Unexpected value.{CLIC.CLR}')
                        return

        print(f'{CLIC.WRN}ERROR: Item of id = {id} does not exist.{CLIC.CLR}')
        return

    def wipe(self) -> None:
        print('Are you sure you want to wipe every activity? y/n')
        choice: str = input(">").lower()
        match choice:
            case 'y':
                self._activity_list = []
                self.__write_json()
                print('Memory wiped.')
            case 'n':
                print(f'{CLIC.WRN}Aborting...{CLIC.CLR}')
            case _:
                print(f'{CLIC.WRN}ERROR: Unexpected value.{CLIC.CLR}')

    def return_balance(self) -> float:
        # balance is only to be calculated from today's activities
        current_day: str = datetime.datetime.now().strftime("%d/%m/%Y")
        balance: float = 0.
        for activity in self._activity_list[::-1]:
            # traverse the list from the latest elements
            # current format: 15/38/3/02/03/2022 - hours and minutes are padded
            if (activity['time_added'][8:] != current_day):
                break
            balance += activity['weight'] * activity['length']

        return balance

    def __write_json(self) -> None:
        data_file = open('activities.json', 'w+', encoding='utf-8')
        json.dump(self._activity_list, data_file)
        data_file.close()
        self.__update_from_json()

    def __update_from_json(self) -> None:
        data_file = open('activities.json', 'r', encoding='utf-8')
        self._activity_list = json.load(data_file)
        if len(self._activity_list) == 0:
            self._next_id = 0
        else:
            self._next_id = self._activity_list[-1]["id"] + 1

    def format_time(self, value: int) -> str:
        if value < 10:
            return f'0{value}'
        return str(value)
