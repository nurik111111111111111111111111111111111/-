#Создай собственный Шутер!
from random import randint
from pygame import *
fps = 69
game = True
finish = False
clock = time.Clock()
win_height = 700
win_width = 900
score = 0
lost = 0
goal = 10
loost = 5
font.init()
font1 = font.SysFont('Arial', 80)
lose = font1.render('лоооооооооооoooooпаааата', True, (255, 255, 255))
win = font1.render('красаааааааавввввчччиикк!!!!!', True, (255, 255, 255))


phon = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
okno = display.set_mode((win_width, win_height))
display.set_caption('огонь и вода')
okno.blit(phon,(0, 0))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    def fire(self):
        potron = Potron('bullet.png', self.rect.centerx, self.rect.top, 20)
        potrony.add(potron)

class Enemy(GameSprite):               
    direction = 'down'
    def update(self):
        if self.rect.y <= 100:
            self.direction = 'down'        
        if self.direction == 'down':
            self.rect.y += self.speed
            global lost
            if self.rect.y > win_height:
                self.rect.x = randint(80, win_width - 80)
                self.rect.y = 0 
                lost = lost + 1

class Potron(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()




potrony = sprite.Group()
player = Player('rocket.png', 10, 630, 4)
monster1 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monster2 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monster3 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monster4 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monster5 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monster6 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monster7 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monster8 = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
monsters = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
monsters.add(monster6)
monsters.add(monster7)
monsters.add(monster8)


while game != False:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.fire()
        
    if game != False:
        okno.blit(phon,(0, 0))
        player.update()
        monsters.update()
        player.reset()
        monsters.draw(okno)
        potrony.draw(okno)
        potrony.update()
        
        collides = sprite.groupcollide(monsters, potrony, True, True)
        for q in collides:
            score = score+1
            monster = Enemy('ufo.png', randint(1, win_width - 50), 10, randint(1, 2))
            monsters.add(monster)
        if lost >= loost:
            finish == True
            okno.blit(lose, (200, 200))
        if score >= goal:
            finish == True 
            okno.blit(win, (200, 200))


    display.update()
    clock.tick(fps)