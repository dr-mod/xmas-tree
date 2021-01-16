from gpiozero import SPIDevice, SourceMixin
from colorzero import Color, Hue
from statistics import mean
from time import sleep
from random import randrange


class RGBXmasTree(SourceMixin, SPIDevice):
    def __init__(self, pixels=25, mosi_pin=12, clock_pin=25, *args, **kwargs):
        super(RGBXmasTree, self).__init__(mosi_pin=mosi_pin, clock_pin=clock_pin, *args, **kwargs)
        self._value = [(0, 0, 0, 0)] * pixels
        self.pixels = pixels
        self.off()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        start_of_frame = [0] * 4
        end_of_frame = [0] * 5
        pixels = [[0b11100000 | br, b, g, r] for r, g, b, br in value]
        pixels = [i for p in pixels for i in p]
        data = start_of_frame + pixels + end_of_frame
        self._spi.transfer(data)
        self._value = value

    def off(self):
        self.value = ((0, 0, 0, 0),) * self.pixels

    def close(self):
        super(RGBXmasTree, self).close()


if __name__ == '__main__':
    tree = RGBXmasTree()