""" Main

Usage:
  main.py <nb_device_data> <nb_events_data>
  Exemple: >> python3 main.py 20 200
"""
import sys

import TableService
from DeviceServices import DeviceServices
from DeviceSql import DeviceSql
from EventSql import EventSql
from TimeService import TimeService


def main(dev_data: int, event_data: int):
    timeSrv = TimeService("2020-01-01 00:00:00", "2020-04-01 23:59:59", "%Y-%m-%d %H:%M:%S")

    my_events = ['homme', 'bouquetin', 'chamois', 'loup', 'loup', 'marmotte', 'Chouette', 'lièvre', 'lièvre']
    deviceSrv = DeviceServices(my_events)

    deviceSQL = DeviceSql(timeSrv, deviceSrv, 'device')
    eventSQL = EventSql(timeSrv, deviceSrv, 'event')

    generate_table_data(deviceSQL, dev_data)
    generate_table_data(eventSQL, event_data)

    eventSQL.get_sql_table()
    deviceSQL.get_sql_table()


def generate_table_data(table: TableService, nb_events: int):
    # format outputs
    output = ""

    for i in range(0, nb_events):
        output += table.get_values()
        output += "\n"

    print(output)

    # Write inside a file
    with open("results/res_" + table.get_tablename() + ".sql", "w") as f:
        f.write(output)
    print("Result saved in file: 'results/res_" + table.get_tablename() + ".sql'.")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <nb_device_data> <nb_events_data>")
        print("Example: python3 main.py 20 200")
    else:
        dev_data = int(sys.argv[1])
        event_data = int(sys.argv[2])
        main(dev_data, event_data)
