from datetime import datetime

def temp():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    start_time = ((int)(now.strftime("%H")) * 60) + (int)(now.strftime("%M")) #Run when "Clock in" pressed"
    end_time = ((int)(now.strftime("%H")) * 60) + (int)(now.strftime("%M")) #Run when "Clock out" is pressed

    print(start_time)
    print("Current Time =", current_time)



def resetVal():
    a = ""
    b = ""
    return a, b
StartTime = 0
EndTime = 0

#print(datetime.now().minute())
"""
class timer:
    def __init__(self):
        self.start = None



def clockIn(ClockIn):
    if ClockIn == True:
        return
    else:
        self.start = datetime.now().minute()
        ClockIn = True
        return 


def clockOut(ClockOut):
    if ClockOut == True:
        return
    else:
        self.start = None
        ClockOut = True
        return 
   """