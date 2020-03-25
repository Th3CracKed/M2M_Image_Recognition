from DeviceServices import DeviceServices
from DeviceSql import DeviceSql
from EventSql import EventSql
from SqlService import SqlService
from TimeService import TimeService


if __name__ == '__main__':
    timeSrv = TimeService("2020-01-01 00:00:00", "2020-04-01 23:59:59", "%Y-%m-%d %H:%M:%S")

    my_events = ['homme', 'bouquetin', 'chamois', 'loup', 'loup', 'marmotte', 'Chouette', 'lièvre', 'lièvre']
    deviceSrv = DeviceServices(my_events)

    deviceSQL = DeviceSql(timeSrv, deviceSrv, 'device')
    eventSQL = EventSql(timeSrv, deviceSrv, 'event')

    SqlService.generate_table_data(deviceSQL, 20)
    SqlService.generate_table_data(eventSQL, 2000)


    eventSQL.get_sql_table()
    deviceSQL.get_sql_table()
