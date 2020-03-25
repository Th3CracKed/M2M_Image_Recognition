from TableService import TableService


class EventSql(TableService):

    def __init__(self, timesrv, devsrv, tablename):
        super().__init__(timesrv, devsrv, tablename)

    def get_values(self):
        return "0," + self.devsrv.get_detetion_accuracy() + "," + self.devsrv.get_camera_event_name() + ",\'" + self.timesrv.get_timestamp() + "\'"

    def get_sql_table(self):
        print("""
               CREATE TABLE events (
                    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    accuracy FLOAT(30) NOT NULL,
                    entity VARCHAR(30) NOT NULL,
                    time TIMESTAMP NOT NULL
                    );
           """)