from gamelib import *

green = (115,190,50)
die = Sound("sfx\\die.ogg",1)
hit = Sound("sfx\\hit.ogg",2)
point = Sound("sfx\\point.ogg",3)
swooshing = Sound("sfx\\swooshing.ogg",4)
wing = Sound("sfx\\wing.ogg",5)

class Bird(object):
    def __init__(self,game):
        self.game = game
        #self.game.setSound(wing)
        self.graphics = Animation("img\\bird\\bird ",3,self.game,frate=0.3)
        self.graphics.y = self.game.height/2
        self.graphics.moveTo(100,self.graphics.y)

    def fly(self):
            #self.game.stopSound()
            self.graphics.y += 2
            self.graphics.moveTo(100,self.graphics.y)
            self.graphics.draw()
           
    def move(self):
            self.graphics.y -= 5
            self.fly()
            wing.play()
            #self.game.playSound()
            
    #executed on death
    def reset(self):
        self.graphics.y = self.game.height/2
        self.graphics.moveTo(100,self.graphics.y)
        self.graphics.draw()

class Pipe(object):
    def __init__(self,game,offset,speed):
        self.game = game
        self.speed = speed
        self.GAP = 100
        self.passed = False
        self.x = game.right + offset
        #self.y = randint(-90,135)
        self.y = randint(-30,95)
        self.pipeTOP = Image("img\\pipe_top.png",self.game) #Y-axis Min: -100 Max: 135
        self.pipeBOT = Image("img\\pipe_bot.png",self.game) #Y-axis Min: 365 Max: 260

    #draws the wall
    def create(self):
        self.pipeTOP.moveTo(self.x,self.y)
        self.pipeBOT.moveTo(self.x,(self.y+270)+self.GAP)
        self.passed = False

    #scrolls the wall    
    def move(self):
        self.pipeTOP.moveX(-self.speed)
        self.pipeTOP.draw()
        self.pipeBOT.moveX(-self.speed)
        self.pipeBOT.draw()

    def isOffScreen(self):
        self.x = self.x - self.speed
        if self.x <= -10:
            return True
    
    #executed on death
    def reset(self):
        self.x = self.game.right
        #self.y = randint(-90,135)
        self.y = randint(-30,95)
        self.create()

    def clear(self,pos):
        self.x = (self.game.right+50) + (self.game.width/3*pos)
        self.create()
