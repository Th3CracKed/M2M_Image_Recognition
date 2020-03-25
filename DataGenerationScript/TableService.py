from DeviceServices import DeviceServices
from TimeService import TimeService
from abc import ABC, abstractmethod


class TableService(ABC):
    timesrv: TimeService
    devsrv: DeviceServices
    tablename: str

    def __init__(self, timesrv, devsrv, tablename):
        self.timesrv = timesrv
        self.devsrv = devsrv
        self.tablename = tablename

    @abstractmethod
    def get_values(self):
        pass

    def get_tablename(self):
        return self.tablename
