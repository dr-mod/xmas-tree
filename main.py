from modified_tree import RGBXmasTree
from time import sleep
from colorzero import Color, Hue
from random import randrange
import datetime
from INA import INA219


def brigtness():
    return randrange(2) * 5 + 1


tree = RGBXmasTree()
ina219 = INA219(addr=0x43)

step = 0
bus_voltage = ina219.getBusVoltage_V()
print("Percent:       {:3.1f}%".format(ina219.getCharge()))
print("Load Voltage:  {:6.3f} V".format(bus_voltage))
try:
    while True:
        now = datetime.datetime.now()
        # if now.hour >= 10 or (now.hour == 9 and now.minute >= 30):
        if True:
            p = [[0, 0, 0, 0], ] * 25
            for i in range(step % 3, len(p), 3):
                p[i] = [0, 255, 0, brigtness()]
            for i in range((step + 1) % 3, len(p), 3):
                p[i] = [255, 0, 0, brigtness()]
            for i in range((step + 2) % 3, len(p), 3):
                p[i] = [0, 0, 255, brigtness()]
            tree.value = p
            step = step + 1
            sleep(0.1)
        else:
            tree.off()
            sleep(60)
except KeyboardInterrupt:
    tree.close()
tree.close()

