from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height, speed):
        super().__init__()
        self.picture = transform.scale(image.load(picture), (x, y))
        self.speed = speed
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    def draw_sprite(self):
        win.blit(self.picture, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < winWidth - 80:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < winWidth - 80:
            self.rect.y += self.speed


backColor = (102, 255, 178)
winHeight = 700
winWidth = 500
game = True
finish = False
FPS = 60
clock = time.Clock()
racket = 'racket.png'
ball = 'ball.png'

font1 = font.SysFont('Arial', 70)
winnerRight = font1.render('Right player win!', True, (255, 255, 255))
winnerLeft = font1.render('Left player win!', True, (255, 255, 255))

win = display.set_mode((winHeight, winWidth))
win.fill(backColor)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    #win.fill(backColor)

    racketLeft.update_left()
    racketRight.update_right()






    racketLeft.draw_sprite()
    racketRight.draw_sprite()
    ball.draw_sprite()




    display.update()
    clock.tick(FPS)
