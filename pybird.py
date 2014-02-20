from pybirdClass import *

def gameOverMSG():
    game.drawText("DEAD! Press ESC to quit",275,150,white,"update")
    #game.over = True

game = Game(700,500,"PyBird",30)
bk = Image("img\\day.png",game)
bar = Animation("img\\bar\\bar ",3,game,10)
bar.moveY(200)
s = Shape(game)

bird = Bird(game)
pipe = Pipe(game)

pipe.draw()

#Game Loop
while not game.over:
    game.processInput()
    bk.draw()
    pipe.move()
    bar.draw()

    #Collision detection problem ex
    s.drawRect(red,bird.graphics.x-17, bird.graphics.y-12, bird.graphics.width,bird.graphics.height,1)
    s.drawRect(red,pipe.pipeTOP.x-26,pipe.pipeTOP.y-135,pipe.pipeTOP.width,pipe.pipeTOP.height,1)
    s.drawRect(red,pipe.pipeBOT.x-26,pipe.pipeBOT.y-135,pipe.pipeBOT.width,pipe.pipeBOT.height,1)
    
    if pipe.isOffScreen():
        pipe.reset()
        
    if keys.Pressed[K_SPACE]:
        bird.move()
    else:
        bird.fly()

    if bird.collidedWith(pipe.pipeTOP) or bird.collidedWith(pipe.pipeBOT):
           gameOverMSG()
        
    game.update(60)
  
game.quit()
