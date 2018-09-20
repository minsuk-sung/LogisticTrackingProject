import struct
import random


str = 'aabbcc'
struct.unpack

def reddensity(x):
    y = int(x * 255)
    rgb = (y, 0, 0)
    hexnumber = bytes.hex(struct.pack('BBB',*rgb))
    return '#'+ hexnumber

def randomcolor():
    rgb = []
    for i in range(3):
        rgb.append(random.randrange(256))

    hexnumber = bytes.hex(struct.pack('BBB', *rgb))
    return '#' + hexnumber


if __name__ == "__main__":
    print(reddensity(0.3))
    print(randomcolor())