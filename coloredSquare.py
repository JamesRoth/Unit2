#James Roth
#2/2/18
#coloredSquare.py - graphics and RGB

from ggame import *

color=int(input("Red (1), yellow (2), green (3), or blue (4)?: "))
if color==1:
    red=Color(0xff0000,1)
    line=LineStyle(3,red)
    rectangle=RectangleAsset(100,100,line,red)
elif color==2:
    yellow=Color(0xffff00,1)
    line=LineStyle(3,yellow)
    rectangle=RectangleAsset(100,100,line,yellow)
elif color==3:
    green=Color(0x008000,1)
    line=LineStyle(3,green)
    rectangle=RectangleAsset(100,100,line,green)
else:
    blue=Color(0x0000FF,1)
    line=LineStyle(3,blue)
    rectangle=RectangleAsset(100,100,line,blue)

Sprite(rectangle)
myApp=App()
myApp.run()