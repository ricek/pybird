from pybirdClass import *

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

quit = False
#Game Loop
while not quit:
    game.processInput()
    
    #Main Loop
    while not game.over:
        game.processInput()
        bk.draw()
        for x in range(len(pipes)):
            pipes[x].move()
            if pipes[x].isOffScreen():
                pipes[x].reset()
            if bird.graphics.collidedWith(pipes[x].pipeTOP,"rectangular") or \
            bird.graphics.collidedWith(pipes[x].pipeBOT,"rectangular"):
                game.over = True
            if pipes[x].pipeTOP.right < bird.graphics.left:
                game.score += 1
                
        bar.draw()
        
        if bird.graphics.y > game.top and bird.graphics.y < bar.top:  
            if keys.Pressed[K_SPACE]:
                bird.move()
            else:
                bird.fly()
        else:
            game.over = True

        game.displayScore()   
        game.update(60)
    #End Main Loop
        
    game.drawText("DEAD! ESC to quit / SPACE to continue",200,150,white)    
    if keys.Pressed[K_ESCAPE]:
        quit = True
    if keys.Pressed[K_SPACE]:
        game.over = False
        bird.reset()
                
    game.update(60)
#End Game Loop
    
game.quit()
