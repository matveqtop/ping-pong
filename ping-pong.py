from pygame import *
from random import randint
class Sprite(sprite.Sprite):
    def __init__(self, Image, xize, yize, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(Image), (xize, yize))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def updatered(self):
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 380:
            self.rect.y += self.speed
    def updateBlue(self):
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 380:
            self.rect.y += self.speed
    def otris(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Ball(sprite.Sprite):
    def __init__(self, Image, xize, yize, sx, sy, x, y):
        super().__init__()
        self.image = transform.scale(image.load(Image), (xize, yize))
        self.speedx = sx
        self.speedy = sy
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def otris(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
game_width = 700
game_hight = 500
window = display.set_mode((game_width, game_hight))
display.set_caption("пинг-понг")
background = transform.scale(image.load('ping-pong.jpg'), (game_width,game_hight))
zastavka = transform.scale(image.load('zastavka.jpg'), (game_width, game_hight))
redpong = Sprite('rocred.png', 80, 120, 5, 10, 200)
bluepong = Sprite('rocblue.png', 80, 120, 5, 607, 200)
a = randint(1,2)
b = randint(1,2)
if a == 1:
    sx = 5
    c = 1
else:
    sx = -5
    c = 0
if b == 1:
    sy = 5
else:
    sy = -5
ball = Ball('BALL.png', 70, 50, sx, sy, 315, 225)
font.init()
font1 = font.SysFont("Arial", 23)
font2 = font.SysFont("Arial", 70)
finish1 = font2.render('Победил красный!', 1, (255, 0, 0))
finish2 = font2.render('Победил синий!', 1, (0, 0, 255))
game = True
finish = True
score1 = 0
score2 = 0
a = 0
Clock = time.Clock()
FPS = 60
keys_pressed = key.get_pressed()
text_zas =font1.render('нажмите "r" чтобы начать', 1, (234, 204, 141))
while game:
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if keys_pressed[K_e]:
            ball.rect.x = 315
            ball.rect.y = 225
            redpong.rect.x = 10
            redpong.rect.y = 200
            bluepong.rect.x = 607
            bluepong.rect.y = 200
            score1 = 0
            score2 = 0
            a = 0
            finish = True
    if score1 == 10:
        window.blit(background, (0, 0))
        window.blit(finish1, (50, 150))
        R = font1.render('нажмите "e", чтобы начать занаво', 1, (255, 0, 0))
        window.blit(R, (175, 250))
    if score2 == 10:
        window.blit(background, (0, 0))
        window.blit(finish2, (100, 150))
        R = font1.render('нажмите "e", чтобы начать занаво', 1, (0, 0, 255))
        window.blit(R, (175, 250))
    if a == 0:
        window.blit(zastavka, (0,0))
        window.blit(text_zas, (215, 475))
        if keys_pressed[K_r]:
            finish = False
            a = 1
    if finish != True:
        tscore1 = font1.render('счёт красных:' + str(score1), 1, (255,0,0))
        tscore2 = font1.render('счёт синих:' + str(score2), 1, (0,0,255))
        window.blit(background, (0, 0))
        window.blit(tscore1, (10, 10))
        window.blit(tscore2, (550, 10))
        ball.otris()
        ball.update()
        redpong.otris()
        redpong.updatered()
        bluepong.otris()
        bluepong.updateBlue()
        if sprite.collide_rect(redpong, ball) and c == 0:
            ball.speedx *= -1
            c += 1
        if sprite.collide_rect(bluepong, ball) and c == 1:
            ball.speedx *= -1
            c -= 1
        if ball.rect.y >= 450 or ball.rect.y <= 0:
            ball.speedy *= -1
        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x = 315
            ball.rect.y = 225
        if ball.rect.x > 675:
            score1 += 1
            ball.rect.x = 315
            ball.rect.y = 225
        if score1 == 10 or score2 == 10:
            finish = True
    display.update()
    Clock.tick(FPS) 