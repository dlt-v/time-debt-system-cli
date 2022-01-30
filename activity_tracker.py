import json


class Tracker():
    _activity_list = []
    _next_id = 0

    def add_activity(self, activity):

        # new_json_data = self.read_json()

        new_activity = {
            'id': self._next_id,
            'name': activity['name'],
            'weight': activity['weight'],
            'length': activity['length'],
        }
        self._next_id += 1
        self._activity_list.append(new_activity)

        # self.write_json(new_json_data)

    def list_activities(self):
        for activity in self._activity_list:
            print(
                f"{activity['id'] + 1}.\t\"{activity['name']}\":\t {activity['length']}")
        print()

    def delete_activity(self, id):
        pass

    def return_balance(self):
        balance = 0
        for activity in self._activity_list:
            balance += activity['weight'] * activity['length']

        return balance

    def read_json(self):
        with open('list.json', 'r') as file:
            data = json.load(file)

        print(data)
        return data

    def write_json(self, data):
        with open('list.json', 'w') as file:
            data = json.dump(file, data)
