import struct

str = 'aabbcc'
struct.unpack

def reddensity(x):
    y = int(x * 255)
    rgb = (y, 0, 0)
    hexnumber = bytes.hex(struct.pack('BBB',*rgb))
    return '#'+ hexnumber