from gamelib import *

green = (115,190,50)

class Bird(object):
    def __init__(self,game):
        self.game = game
        self.bird = Animation("img\\bird\\bird ",3,self.game,frate=10)
        self.bird.y = self.game.height/2
        self.bird.moveTo(100,self.bird.y)

    def fly(self):
        if self.bird.y >= 0 and self.bird.y <= 380:
            self.bird.y += 1
            self.bird.moveTo(100,self.bird.y)
            self.bird.draw()
           
    def move(self):
        if self.bird.y >= 0 and self.bird.y <= 380:
            self.bird.y -= 3
            self.fly()
        
    def reset(self):
        self.bird.y = self.game.height/2
        self.bird.moveTo(100,self.bird.y)
        self.bird.draw()

class Pipe(object):
    def __init__(self,game):
        self.game = game
        self.x = game.right
        self.y = randint(-90,135)
        self.speed = -5
        self.GAP = 100

        '''
        s.drawRect(green,250,0,50,100)
        s.drawRect(black,250,0,50,100,1)
        s.drawRect(green,230,90,90,40)
        s.drawRect(black,230,90,90,40,1)
    
        s.drawRect(green,game.right-80,0,50,100)
        s.drawRect(black,game.right-80,0,50,100,2)
        s.drawRect(green,game.right-100,90,90,40)
        s.drawRect(black,game.right-100,90,90,40,2)
        '''

    def draw(self):
        self.pipeTOP = Image("img\\pipe_top.png",self.game) #Y-axis Min: -100 Max: 135
        self.pipeTOP.moveTo(self.x,self.y)
        self.pipeBOT = Image("img\\pipe_bot.png",self.game) #Y-axis Min: 365 Max: 260
        self.pipeBOT.moveTo(self.x,(self.y+270)+self.GAP)
        
    def move(self):
        self.pipeTOP.moveX(self.speed)
        self.pipeTOP.draw()
        self.pipeBOT.moveX(self.speed)
        self.pipeBOT.draw()

    def isOffScreen(self):
        self.x = self.x + self.speed
        if self.x <= -20:
            return True

    def reset(self):
        self.x = self.game.right
        self.y = randint(-90,135)
        self.draw()
