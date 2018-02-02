#James Roth
#2/2/18
#coloredSquare.py - graphics and RGB

from ggame import *

color=int(input("Red (1), yellow (2), green (3), or blue (4) ?"))
if color==1:
    red=Color(0xff0000,1)
    line=LineStyle(3,red)
    rectangle=RectangleAsset(100,100,line,red)
elif color==2:
    red=Color(0xff0000,1)
    line=LineStyle(3,red)
    rectangle=RectangleAsset(100,100,line,red)
elif color==3:
    red=Color(0xff0000,1)
    line=LineStyle(3,red)
    rectangle=RectangleAsset(100,100,line,red)
else:
    red=Color(0xff0000,1)
    line=LineStyle(3,red)
    rectangle=RectangleAsset(100,100,line,red)


Sprite(rectangle)
myApp=App()
myApp.run()


