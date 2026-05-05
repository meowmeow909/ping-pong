from pygame import *
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height, speed):
        super().__init__()
        self.picture = transform.scale(image.load(picture), (width, height))
        self.speed = speed
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
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
speedX = 3
speedY = 3

font1 = font.SysFont('Arial', 70)
winnerRight = font1.render('Right player win!', True, (255, 255, 255))
winnerLeft = font1.render('Left player win!', True, (255, 255, 255))

win = display.set_mode((winHeight, winWidth))
win.fill(backColor)

racketLeft = Player(racket, 50, winWidth/2, 60, 120, 4)
racketRight = Player(racket, winHeight-50, winWidth/2, 60, 120, 4)
ball = Player(ball, winWidth/2, winHeight/2, 50, 50, 4)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    win.fill(backColor)
    
    racketLeft.draw_sprite()
    racketRight.draw_sprite()
    ball.draw_sprite()
    
    racketLeft.update_left()
    racketRight.update_right()
    
    ball.rect.x += speedX
    ball.rect.y += speedY
    
    if sprite.collide_rect(ball, racketLeft) or sprite.collide_rect(ball, racketRight):
        speedX *= -1
       
    if ball.rect.y < 0 or ball.rect.y > winWidth:
        speedY *= -1

    if ball.rect.x <= 0:
        win.blit(winnerLeft, (200, 200))
        game = False
    elif ball.rect.x >= winHeight:
        win.blit(winnerRight, (200, 200))
        game = False

    display.update()
    clock.tick(FPS)
