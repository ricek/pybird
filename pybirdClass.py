import pygame
from gamelib import *

green = (115,190,50)
die = "sfx\\die.mp3"
hit = "sfx\\hit.mp3"
point = "sfx\\point.mp3"
swooshing = "sfx\\swooshing.mp3"
wing = "sfx\\wing.mp3"

class Bird(object):
    def __init__(self,game):
        self.game = game
        self.game.setSound(wing)
        self.graphics = Animation("img\\bird\\bird ",3,self.game,frate=10)
        self.graphics.y = self.game.height/2
        self.graphics.moveTo(100,self.graphics.y)
        self.graphics.rect = pygame.Rect(self.graphics.x-17, self.graphics.y-12, self.graphics.width,self.graphics.height)

    def fly(self):
        if self.graphics.y >= 0 and self.graphics.y <= 380:
            self.game.stopSound()
            self.graphics.y += 1
            self.graphics.moveTo(100,self.graphics.y)
            self.graphics.draw()
        else:
            self.reset()
           
    def move(self):
        if self.graphics.y >= 0 and self.graphics.y <= 380:
            self.graphics.y -= 3
            self.fly()
            self.game.playSound()
        else:
            self.reset()       

    def collidedWith(self,obj):
        self.obj = obj
        self.obj.rect = pygame.Rect(self.obj.x-26, self.obj.y-135, self.obj.width,self.obj.height)
        if self.graphics.rect.colliderect(self.obj.rect):
            return True

    #executed on death
    def reset(self):
        self.graphics.y = self.game.height/2
        self.graphics.moveTo(100,self.graphics.y)
        self.graphics.draw()

class Pipe(object):
    def __init__(self,game):
        self.game = game
        self.x = game.right
        self.y = randint(-90,135)
        self.speed = 3
        self.GAP = 100
        self.pipeTOP = Image("img\\pipe_top.png",self.game) #Y-axis Min: -100 Max: 135
        self.pipeBOT = Image("img\\pipe_bot.png",self.game) #Y-axis Min: 365 Max: 260

        '''
        self.s.drawRect(green,250,0,50,100)
        self.s.drawRect(black,250,0,50,100,1)
        self.s.drawRect(green,230,90,90,40)
        self.s.drawRect(black,230,90,90,40,1)
        
        s.drawRect(green,game.right-80,0,50,100)
        s.drawRect(black,game.right-80,0,50,100,2)
        s.drawRect(green,game.right-100,90,90,40)
        s.drawRect(black,game.right-100,90,90,40,2)
        '''

    #draws the wall
    def draw(self):
        self.pipeTOP.moveTo(self.x,self.y)
        self.pipeBOT.moveTo(self.x,(self.y+270)+self.GAP)

    #scrolls the wall    
    def move(self):
        self.pipeTOP.moveX(-self.speed)
        self.pipeTOP.draw()
        self.pipeBOT.moveX(-self.speed)
        self.pipeBOT.draw()

    def isOffScreen(self):
        self.x = self.x - self.speed
        if self.x <= -20:
            return True

    #executed on death
    def reset(self):
        self.x = self.game.right
        self.y = randint(-90,135)
        self.draw()
