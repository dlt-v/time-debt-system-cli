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

    def list_activities(self) -> None:
        for activity in self._activity_list:
            activity_time: datetime.datetime = datetime.datetime.strptime(
                activity['time_added'], "%H/%M/%w/%d/%m/%Y")
            print(activity_time)
            print(datetime.datetime.now())
            delta: datetime.timedelta = datetime.datetime.now() - activity_time
            # print(delta.)
            print(
                f"{activity['id']}.\t\"{activity['name'][0:15]}{ '...' if len(activity['name']) > 15 else ''}\":\t{activity['length']}\t{activity['time_added']}\n")

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
        balance: float = 0.
        for activity in self._activity_list:
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
