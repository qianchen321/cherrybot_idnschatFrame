import time
import datetime


def getTimeStamp():
    seconds = int(time.time() // 100)
    milliseconds = int(datetime.datetime.now().microsecond)
    time_stamp = str(seconds) + str(milliseconds)
    return time_stamp


def TimeStampToTime(time_stamp13):
    now_time = datetime.datetime.fromtimestamp(time_stamp13/1000)
    return str(now_time)[:-4]
