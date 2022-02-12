import json
from cli_colors import cli_colors

CLIC = cli_colors()


class Tracker():
    _next_id = 0
    _activity_list = []

    def __init__(self) -> None:
        self.__update_from_json()

    def add_activity(self, activity) -> None:

        new_activity = {
            'id': self._next_id,
            'name': activity['name'],
            'weight': activity['weight'],
            'length': activity['length'],
        }
        self._next_id += 1
        self._activity_list.append(new_activity)
        self.__write_json()

    def list_activities(self) -> None:
        for activity in self._activity_list:
            print(
                f"{activity['id']}.\t\"{activity['name']}\":\t {activity['length']}\n")

    def delete_activity(self, id) -> None:
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
