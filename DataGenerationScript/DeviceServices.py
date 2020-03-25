import random
import uuid
from typing import List


class DeviceServices:
    events: List[str]

    def __init__(self,events=['loup', 'lapin']):
        self.events = events

    def get_dev_id(self) -> str:
        hashVal = uuid.uuid4().hex
        return str(hashVal[:8])

    def get_gps(self):
        return str("" + self.get_latitude() + "," + self.get_longitude())

    @staticmethod
    def get_latitude():
        lat = random.uniform(43, 49)
        lat = round(lat, 8)
        return str(lat)

    @staticmethod
    def get_longitude():
        long = random.uniform(-1, 7)
        long = round(long, 8)
        return str(long)

    def get_detetion_accuracy(self):
        long = random.uniform(0, 1)
        long = round(long, 2)
        return str(long)

    def get_camera_event_name(self) -> int:
        rend_event = random.randint(0, len(self.events) - 1)
        return str("\'" + self.events[rend_event] + "\'")

    def get_battery(self) -> int:
        bat = random.randint(10, 100)
        return str(bat)
