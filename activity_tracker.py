import json
from cli_colors import cli_colors

CLIC = cli_colors()


class Tracker():
    _next_id = 0
    _activity_list = []

    def add_activity(self, activity):

        new_activity = {
            'id': self._next_id,
            'name': activity['name'],
            'weight': activity['weight'],
            'length': activity['length'],
        }
        self._next_id += 1
        self._activity_list.append(new_activity)

    def list_activities(self):
        for activity in self._activity_list:
            print(
                f"{activity['id'] + 1}.\t\"{activity['name']}\":\t {activity['length']}")
        print()

    def delete_activity(self, id):
        for i, activity in enumerate(self._activity_list):
            if activity["id"] == id:
                print('Are you sure you want to delete this item? y/n')
                choice = input(">").lower()
                match choice:
                    case 'y':
                        del self._activity_list[i]
                        return
                    case 'n':
                        print(f'{CLIC.WRN}Aborting...{CLIC.CLR}')
                        return
                    case _:
                        print(f'{CLIC.WRN}ERROR: Unexpected value.{CLIC.CLR}')
                        return

        print(f'{CLIC.WRN}ERROR: Item of that id does not exist.{CLIC.CLR}')
        return

        # find index of the object with an id of ID
        # delete that object from the list

    def return_balance(self):
        balance = 0
        for activity in self._activity_list:
            balance += activity['weight'] * activity['length']

        return balance
