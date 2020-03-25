import random
import time


class TimeService:
    start: str
    end: str
    format: str

    def __init__(self, start="2020-01-01 00:00:00", end="2020-12-30 23:59:59", format="%Y-%m-%d %H:%M:%S"):
        self.start = start
        self.end = end
        self.format = format

    @staticmethod
    def str_time_prop(start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """

        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(format, time.localtime(ptime))

    def get_timestamp(self):
        return self.str_time_prop(self.start, self.end, self.format, random.random())