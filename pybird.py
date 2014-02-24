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
    
    if pipe.isOffScreen():
        pipe.reset()
        
    if keys.Pressed[K_SPACE]:
        bird.move()
    else:
        bird.fly()

    if bird.graphics.collidedWith(pipe.pipeTOP,"rectangular") or bird.graphics.collidedWith(pipe.pipeBOT,"rectangular"):
           gameOverMSG()
        
    game.update(60)
  
game.quit()
