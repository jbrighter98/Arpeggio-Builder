AppHeight = 600
AppWidth = 500
from virtualneck import Neck



def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex


def hex2rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))


def shade(hexcolor, shadeAmount):
    working = hex2rgb(hexcolor)
    working = [(i - shadeAmount) if ((i - shadeAmount) >= 0) else 0 for i in
               working]  ### ASSURES VALUES DONT GO BELOW 0 #####
    c = rgb2hex(working[0], working[1], working[2])
    return c

def lightn(hexcolor, lightAmount = 40):
    working = hex2rgb(hexcolor)
    working = [(i + lightAmount) if ((i + lightAmount) <= 255) else 255 for i in
               working]  ### ASSURES VALUES DONT GO BELOW 0 #####
    c = rgb2hex(working[0], working[1], working[2])
    return c

red = rgb2hex(255,81,81)
green = rgb2hex(177, 246, 156)
blue = rgb2hex(164, 235, 240)
yellow = rgb2hex(246, 249, 163)

gray = rgb2hex(200,200,200)
darkGray =  rgb2hex(50,50,50)
black = rgb2hex(0,0,0)
lightGray = rgb2hex(190,190,190)
white = rgb2hex(255,255,255)

### origonal ###  color_pallet = ['#BA4141', '#95FA92', '#4196C0', '#DCEF8F'] ### for NOTES R, 3, 5, 7
#color_pallet = [rgb2hex(255,81,81), rgb2hex(177, 246, 156), rgb2hex(164, 235, 240), rgb2hex(246, 249, 163)]
#color_pallet = [red, green, blue, yellow]
####           [  'red'     'green'     'blue'    'yellow']
####            [   1         3           5          7    ]



neckColor =     '#C9B5A4'   # rgb2hex(201, 181, 164)
#print(hex2rgb(neckColor))
fretColor =     '#666666'   # rgb2hex(102, 102, 102)
fretOutline =   '#000000'   # rgb2hex(0,0,0)

stringOutline = '#444444'       # rgb2hex(68, 68, 68)
stringColor =   '#757575'   # rgb2hex(117, 117, 117)

markerCenter = '#FCFFEB'    # rgb2hex(252, 255, 235)
markerOutline = '#797367'       # rgb2hex(121, 115, 103)

highlights = '#FFFFFF'      # rgb2hex(255,255,255)
stringHighlights = '#D0D0D0'    # rgb2hex(208,208,208)


CB_root = lightn(rgb2hex(136, 34, 85))
CB_third = lightn(rgb2hex(34, 136, 51))
CB_fifth = lightn(rgb2hex(102, 204, 238))
CB_seventh = lightn(rgb2hex(204, 187, 68))


CB2_root = lightn(rgb2hex(236, 5, 120))
CB2_third = lightn(rgb2hex(42, 181, 115))
CB2_fifth = lightn(rgb2hex(0, 173, 239))
CB2_seventh = lightn(rgb2hex(255, 254, 0))
Default_Colors = [ red, green, blue, yellow ]

ColorBlind_Colors = [ CB_root, CB_third, CB_fifth, CB_seventh ]
ColorBlind_Colors = [ CB2_root, CB2_third, CB2_fifth, CB2_seventh ]



color_pallet = Default_Colors[:]