from pybirdClass import *

def gameOverMSG():
    game.drawText("DEAD! Press ESC to quit",275,150,white)
    game.over = True

game = Game(700,500,"PyBird",30)
bk = Image("img\\day.png",game)
bar = Animation("img\\bar\\bar ",3,game,10)
bar.moveY(200)
s = Shape(game)

bird = Bird(game)
pipes = []

for x in range(3):
    pipes.append(Pipe(game,(game.width/3*x),3))
    pipes[x].create()

#Game Loop
while not game.over:
    game.processInput()
    bk.draw()
    for x in range(len(pipes)):
        pipes[x].move()
        if pipes[x].isOffScreen():
            pipes[x].reset()
        if bird.graphics.collidedWith(pipes[x].pipeTOP,"rectangular") or bird.graphics.collidedWith(pipes[x].pipeBOT,"rectangular"):
            gameOverMSG()
    bar.draw()
   
    if keys.Pressed[K_SPACE]:
        bird.move()
    else:
        bird.fly()
        
    game.update(60)
  
game.quit()
