from pybirdClass import *

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
    if pipe.isOffScreen():
        pipe.reset()

    bar.draw()
    

    if keys.Pressed[K_SPACE]:
        bird.move()
    else:
        bird.fly()

    #if bird.collidedWith(pipe):
        #game.over = True

    #if bird.isOffScreen():
        #game.drawText("DEAD! Try again\nPress ESC to quit",150,250)
        #bird.resetBird()

    game.update(60)
    

game.quit()

