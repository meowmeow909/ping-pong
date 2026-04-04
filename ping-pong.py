from pygame import *

backColor = (102, 255, 178)
winHeight = 700
winWidth = 500
game = True
FPS = 60
clock = time.Clock()

win = display.set_mode((winHeigh, winWidth))
win.fill(backColor)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False




    display.update()
    clock.tick(FPS)
