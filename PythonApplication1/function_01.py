def resetVal():
    a = ""
    b = ""
    return a, b


class Time():
    time.s = 0
    time.m = 0
    time.h = 0



def clockIn(ClockIn):
    if ClockIn == True:
        return
    else:
        import time
        time.s = time.time()
        time.m = time.time() // 60
        time.h = time.time() // 3600
        ClockIn = True
        return time.s, time.m, time.h


def clockOut(ClockOut):
    if ClockOut == True:
        return
    else:
        time.s = 0
        time.m = 0
        time.h = 0
        ClockOut = True
        return 
