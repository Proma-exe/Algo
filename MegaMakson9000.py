#-*- coding:utf-8 -*-
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
from finalwin import *
from pygame import *
import random
from math import pi, atan2
from time import sleep
def startgame(x=30):
    screensize = [1280, 720]

    '''def attack():
        randSprite = random.choice(Enemies.sprites())
        randSprite.shoot()'''

    class GameSprite(sprite.Sprite):
        def __init__(self, picture, w, h, x ,y):
            sprite.Sprite.__init__(self)
            self.image = transform.scale(image.load(picture), (w, h))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

    class player(GameSprite):
        def __init__(self, picture, w, h, x ,y):
            GameSprite.__init__(self, picture, w, h, x ,y)
            self.data = (w, h)
        
        def rotate(self):
            """ need to COMPLETE! """
            """ need to COMPLETE! """
            """ need to COMPLETE! """
            
            mouse_x, mouse_y = mouse.get_pos()
            rel_x, rel_y = mouse_x - self.rect.centerx , mouse_y - self.rect.centery
            angle = (180 / pi) * - atan2(rel_y, rel_x) - 90
            self.image = transform.rotate(transform.scale(image.load('image/MegaMakson.png'), self.data), int(angle))
            

            
        def shoot(self):
            bspeed = 50
            m_x, m_y = mouse.get_pos()

            xmul = m_x - self.rect.centerx
            ymul = m_y - self.rect.centery
            dstnc = (xmul**2 + ymul **2)**0.5
            


            if dstnc != 0:
                bulletH = BulletH(
                    'image/Energyball.png', 
                    int(screensize[0]*0.02),
                    int(screensize[0]*0.02),
                    self.rect.centerx - int(screensize[0]*0.02) // 2,
                    self.rect.top,
                    bspeed / dstnc * xmul, # bullet x speed
                    bspeed / dstnc * ymul  # bullet y speed
                    ) 
                bulletsH.add(bulletH)
        


    class Enemy(GameSprite):
        def __init__(self, picture, w, h, x, y, x_speed):
            GameSprite.__init__(self, picture, w, h, x ,y)
            self.x_speed = x_speed
        
        def start(self):
            r = random.randint(0, 3)
            if r == 0:
                self.x_speed = -7; self.y_speed = -7
            elif r == 1:
                self.x_speed = 7; self.y_speed = -7
            elif r == 2:
                self.x_speed = -7; self.y_speed = 7
            elif r == 3:
                self.x_speed = 7; self.y_speed = 7

        def update(self):
            if self.rect.top < 0: self.y_speed *= -1
            if self.rect.left < 0: self.x_speed *= -1
            if self.rect.bottom > (screensize[1]/1.7): self.y_speed *= -1
            if self.rect.right > screensize[0]: self.x_speed *= -1

            self.rect.x += self.x_speed
            self.rect.y += self.y_speed

    class Boom1(GameSprite):
        def __init__(self, picture, w, h, x, y, livetime):
            super().__init__(picture, w, h, x, y)
            self.livetime = livetime
        
        def update(self):
            if self.livetime != 0: self.livetime -= 1
            else: self.kill()



    class BulletH(GameSprite): 
        def __init__(self, picture, w, h, x, y, x_speed, y_speed): 
            super().__init__(picture, w, h, x, y) 
            self.x_speed = x_speed 
            self.y_speed = y_speed 
        def update(self): 
            
            if (self.rect.y <= 0) or (self.rect.left <0) or (self.rect.right > screensize[0]): 
                self.kill()
            hit = sprite.spritecollide(self, Enemies, True)
            if hit:
                self.kill()
                boom = Boom1('image/Boom.png', int(screensize[0]*0.05), int(screensize[0]*0.05), self.rect.left, self.rect.top, 1)
                booms.add(boom)
            self.rect.y += self.y_speed
            self.rect.x += self.x_speed

    window = display.set_mode(screensize)
    display.set_caption('MegaMakson9000 Cosmic Adventures')
    window.fill((255, 255, 255))
    bg = transform.scale(image.load('image/cosmos.jpg'), screensize)
    window.blit(bg, (0, 0))

    Heroes = sprite.Group()
    Enemies = sprite.Group()
    bulletsE = sprite.Group()
    bulletsH = sprite.Group()
    booms = sprite.Group()

    Hero = player(
        'image/MegaMakson.png', 
        int(screensize[0]*0.07), 
        int(screensize[0]*0.07), 
        ((screensize[0]//2) - int(screensize[0]*0.1) // 2), 
        (screensize[1] - screensize[1]//5)
    )
    Heroes.add(Hero)

    fool0 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 1), (screensize[0]//11 * 0), 3)
    fool1 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 2), (screensize[0]//11 * 0), 3)
    fool2 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 3), (screensize[0]//11 * 0), 3)
    fool3 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 4), (screensize[0]//11 * 0), 3)
    fool4 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 5), (screensize[0]//11 * 0), 3)
    fool5 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 6), (screensize[0]//11 * 0), 3)
    fool6 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 7), (screensize[0]//11 * 0), 3)
    fool7 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 8), (screensize[0]//11 * 0), 3)
    fool8 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 9), (screensize[0]//11 * 0), 3)
    fool9 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 10), (screensize[0]//11  * 0), 3)
    fool10 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 1), (screensize[0]//11  * 1), 3)
    fool11 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 2), (screensize[0]//11  * 1), 3)
    fool12 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 3), (screensize[0]//11  * 1), 3)
    fool13 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 4), (screensize[0]//11  * 1), 3)
    fool14 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 5), (screensize[0]//11  * 1), 3)
    fool15 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 6), (screensize[0]//11  * 1), 3)
    fool16 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 7), (screensize[0]//11  * 1), 3)
    fool17 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 8), (screensize[0]//11  * 1), 3)
    fool18 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 9), (screensize[0]//11  * 1), 3)
    fool19 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 10), (screensize[0]//11  * 1), 3)
    fool20 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 1), (screensize[0]//11  * 2), 3)
    fool21 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 2), (screensize[0]//11  * 2), 3)
    fool22 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 3), (screensize[0]//11  * 2), 3)
    fool23 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 4), (screensize[0]//11  * 2), 3)
    fool24 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 5), (screensize[0]//11  * 2), 3)
    fool25 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 6), (screensize[0]//11  * 2), 3)
    fool26 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 7), (screensize[0]//11  * 2), 3)
    fool27 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 8), (screensize[0]//11  * 2), 3)
    fool28 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 9), (screensize[0]//11  * 2), 3)
    fool29 = Enemy('image/Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 10), (screensize[0]//11  * 2), 3)
    Enemies.add(fool0)
    Enemies.add(fool1)
    Enemies.add(fool2)
    Enemies.add(fool3)
    Enemies.add(fool4)
    Enemies.add(fool5)
    Enemies.add(fool6)
    Enemies.add(fool7)
    Enemies.add(fool8)
    Enemies.add(fool9)
    Enemies.add(fool10)
    Enemies.add(fool11)
    Enemies.add(fool12)
    Enemies.add(fool13)
    Enemies.add(fool14)
    Enemies.add(fool15)
    Enemies.add(fool16)
    Enemies.add(fool17)
    Enemies.add(fool18)
    Enemies.add(fool19)
    Enemies.add(fool20)
    Enemies.add(fool21)
    Enemies.add(fool22)
    Enemies.add(fool23)
    Enemies.add(fool24)
    Enemies.add(fool25)
    Enemies.add(fool26)
    Enemies.add(fool27)
    Enemies.add(fool28)
    Enemies.add(fool29)

    
    rech = 0
    recharge = 0
    peew = True
    run = True
    No = False

    for i in Enemies:
        i.start()
    
    while run:
        if rech != 0:
            rech -= 1
        if len(Enemies)==0:
            return FinalWin()
            run = False
        if len(Heroes)==0:
            l = GameSprite('image/lose.jpg', screensize[0], screensize[1], 0, 0)
            l.reset()
            No = True
            
            
        time.delay(40)
        for i in event.get():
            if i.type == QUIT:
                run = False
            elif i.type == KEYDOWN:
                if i.key == K_a:
                    Hero.x_speed = -10
                elif i.key == K_d:
                    Hero.x_speed = 10
                elif i.key == K_s:
                    Hero.y_speed = 10
                elif i.key == K_w:
                    Hero.y_speed = -10
            if i.type == MOUSEBUTTONDOWN:
                if rech == 0:
                    Hero.shoot()
                    rech = 20

            elif i.type == KEYUP:
                if i.key == K_a:
                    Hero.x_speed = 0
                elif i.key == K_d:
                    Hero.x_speed = 0
                elif i.key == K_s:
                    Hero.y_speed = 0
                elif i.key == K_w:
                    Hero.y_speed = 0
            
                    
        if not(No):
            window.fill((255, 255, 255))
            window.blit(bg, (0, 0))
            Hero.rotate()
            Hero.reset()
            for i in Enemies:
                i.update()
                i.reset()
            for i in bulletsH:
                i.update()
                i.reset()
            for i in booms:
                i.reset()
                i.update()

            '''if peew == False:
                attack()
                peew = True
            elif peew:
                recharge += 1
            if recharge >= x:
                peew = False
                recharge = 0'''
            
    
        display.update()
#startgame(10)