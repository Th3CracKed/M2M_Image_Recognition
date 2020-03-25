from TableService import TableService


class DeviceSql(TableService):
    def __init__(self, timesrv, devsrv, tablename):
        super().__init__(timesrv, devsrv, tablename)

    def get_values(self):
        return "0,\'" + self.devsrv.get_dev_id() + "\'," + self.devsrv.get_gps() + "," + self.devsrv.get_battery() + ",\'" + self.timesrv.get_timestamp() + "\'"

    def get_sql_table(self):
        print("""
            CREATE TABLE devices (
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                devEUI VARCHAR(30) NOT NULL,
                latitude FLOAT(30) NOT NULL,
                longitude FLOAT(30) NOT NULL,
                batteryLevel FLOAT(30) NOT NULL,
                time TIMESTAMP NOT NULL
                );
        """)
