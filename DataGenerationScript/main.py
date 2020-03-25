import TableService
from DeviceServices import DeviceServices
from DeviceSql import DeviceSql
from EventSql import EventSql
from TimeService import TimeService


def main():
    timeSrv = TimeService("2020-01-01 00:00:00", "2020-04-01 23:59:59", "%Y-%m-%d %H:%M:%S")

    my_events = ['homme', 'bouquetin', 'chamois', 'loup', 'loup', 'marmotte', 'Chouette', 'lièvre', 'lièvre']
    deviceSrv = DeviceServices(my_events)

    deviceSQL = DeviceSql(timeSrv, deviceSrv, 'device')
    eventSQL = EventSql(timeSrv, deviceSrv, 'event')

    generate_table_data(deviceSQL, 20)
    generate_table_data(eventSQL, 200)

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
    main()
