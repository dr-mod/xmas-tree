from modified_tree import RGBXmasTree
from time import sleep
from random import randrange
import datetime
from INA import INA219
import math


def brigtness():
    return randrange(2) * 5 + 1


tree = RGBXmasTree()
ina219 = INA219(addr=0x43)

step = 0
bus_voltage = ina219.getBusVoltage_V()
external = [[0, 0, 0, 0], ] * 25
try:
    battery = False
    while True:
        now = datetime.datetime.now()
        # if now.hour >= 10 or (now.hour == 9 and now.minute >= 30):
        if True:
            # p = [[0, 0, 0, 0], ] * 25
            p = external
            for i in range(step % 3, len(p), 3):
                e = [0,0,0,0]
                if not battery:
                    e[0] = int((math.sin(step) / 2 + 0.5) * 50)
                    e[1] = int((math.sin(step + 2.09) / 2 + 0.5) * 200)
                    e[2] = int((math.sin(step + 4.18) / 2 + 0.5) * 200)
                else:
                    e[0] = int((math.sin(step / 2) / 2 + 0.5) * 200)
                    # e[1] = int((math.sin(step + 2.09) / 2 + 0.5) * 255)
                    # e[2] = int((math.sin(step + 4.18) / 2 + 0.5) * 255)
                e[3] = 2  # brigtness()
                p[i] = e
            tree.value = p
            step = step + 1
            if (step % 10) == 0:
                battery = ina219.isBattery()
            sleep(0.1)
            external = p

        else:
            tree.off()
            sleep(60)
except KeyboardInterrupt:
    tree.close()
tree.close()

