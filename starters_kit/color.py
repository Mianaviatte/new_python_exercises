class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b):
        red = r
        green = g
        blue = b

    def toHex(self):
        return '#%02x%02x%02x' % (red, green, blue)

class ColorAlpha(Color):
    Alpha = 1

    def __init__(self, r, g, b, a):
        Alpha = a

gray = Color(80, 80, 80) #grey color
redS = ColorAlpha(255, 0, 0, .5) #halfclear red
