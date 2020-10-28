from pylgbst.hub import MoveHub, COLORS, COLOR_NONE, COLOR_RED
from pylgbst.peripherals import Motor
from pylgbst import get_connection_bluegiga
import time

conn = get_connection_bluegiga("Any","00:16:53:AB:7C:25","Dima's hub")
hub = MoveHub(conn)

for device in hub.peripherals:
    print(device)


def callback(clr):
    print("Color has changed: %s" % clr)


hub.led.subscribe(callback)

hub.led.set_color(COLOR_RED)
for color in COLORS:
    hub.led.set_color(color)
    time.sleep(0.5)

hub.led.set_color(COLOR_NONE)
hub.led.unsubscribe(callback)

hub.motor_A.timed(5,1,1)
hub.motor_B.timed(5,-1,-1)

hub.motor_external.timed(seconds=2,end_state=126)