#converts hex value to rgb
def to_rgb(hex):
    return (
        hex >> 16 & 0xFF,
        hex >> 8 & 0xFF,
        hex & 0xFF
    )

#converts rgb value to hex 
def to_hex(rgb):
    return rgb[0] << 16 | rgb[1] << 8 | rgb[2]

#changed brightness in hex 
def adjust_brightness(hex, by=1):
    return to_hex(map(lambda c: int(c * by), to_rgb(hex)))
