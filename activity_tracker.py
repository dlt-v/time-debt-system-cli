class Tracker():
    _activity_list = []
    _next_id = 0

    def add_activity(self, activity):
        new_activity = {
            'id': self._next_id,
            'weight': activity['weight'],
            'length': activity['length']
        }
        self._next_id += 1
        self._activity_list.append(new_activity)

    def list_activities(self):
        for activity in self._activity_list:
            print(
                f"{activity['id']}: {activity['weight']}: {activity['length']}")

    def delete_activity(self, id):
        pass

    def return_balance(self):
        balance = 0
        for activity in self._activity_list:
            balance += activity['weight'] * activity['length']

        return balance
