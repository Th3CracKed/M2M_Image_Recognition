from DeviceServices import DeviceServices
from TableService import TableService
from TimeService import TimeService


class SqlService:
    timesrv: TimeService
    devsrv: DeviceServices

    def __init__(self, timesrv, devsrv):
        self.timesrv = timesrv
        self.devsrv = devsrv

    @staticmethod
    def generate_table_data(table: TableService, nb_events: int):
        # format outputs
        output = ""

        for i in range(0, nb_events):
            output += table.get_values()
            output += "\n"

        print(output)

        # Write inside a file
        with open("results/res_events_" + table.get_tablename() + ".sql", "w") as f:
            f.write(output)
        print("Result saved in file: 'results/res_events_" + table.get_tablename() + ".sql'.")
