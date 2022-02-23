from typing import TypedDict


class NewActivity(TypedDict):
    name: str
    weight: float
    length: float


class Activity(NewActivity):
    id: int
    time_added: str
