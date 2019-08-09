from turtle import *
from datetime import datetime
from time import sleep

bgpic('Clock_background.png')
_prev_minute = int(datetime.now().strftime("%M"))

def get_angle(x):
    now = datetime.now()
    if x == 'hour':
        hour = int(now.strftime("%I"))
        minute = int(now.strftime("%M"))
        angle = (hour - 3) * 30 + minute * 0.5
        return angle
    elif x == 'minute':
        minute = int(now.strftime("%M"))
        angle = (minute - 15 ) * 6
        return angle
    elif x == 'second':
        second = int(now.strftime("%S"))
        angle = (second - 15) * 6
        return angle
    else:
        raise Exception("Wrong argument! Argument to get_angle must be either on of the followings: 'hour', 'minute' or 'second'")


def is_changed():
    global _prev_minute
    
    _cur_minute = int(datetime.now().strftime("%M"))

    if _prev_minute == _cur_minute:
        return False
    else:
        _prev_minute = _cur_minute
        return True

while True:
    clear()
    up()
    home()
    down()
    pensize(10)
    right(get_angle('hour'))
    forward(200)

    up()
    home()
    down()
    pensize(5)
    right(get_angle('minute'))
    forward(200)

    while not is_changed():
        sleep(1)
        
    update()
