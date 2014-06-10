from pybirdClass import *

game = Game(700,500,"PyBird",30)
bk = Image("img\\day.png",game)
bar = Animation("img\\bar\\bar ",3,game,frate=0.1)
bar.moveY(200)
#s = Shape(game)

score_one = Animation("img\\score.png",10,game,34,46)
score_ten = Animation("img\\score.png",10,game,34,46)
score_one.stop()
score_ten.stop()
score_one.moveTo(350,455)
score_ten.visible = False


bird = Bird(game)
pipes = []
quit = False

for x in range(3):
    pipes.append(Pipe(game,(game.width/3*x),3))
    pipes[x].create()

def clearpipes():
    for x in range(len(pipes)):
        pipes[x].clear(x)
        
def startscreen():
    start = True
    bird_init = Animation("img\\bird\\bird ",3,game,frate=0.1)

    while start:
        game.processInput()
        bk.draw()
        bar.draw()
        score_one.f = 0
        score_ten.f = 0
        score_ten.visible = False
        score_one.draw()
        if keys.Pressed[K_SPACE]:
            start = False
            game.over = False
            bird.reset()
        elif keys.Pressed[K_q]:
            quit = True
        bird_init.moveTo(game.width/2,game.height/2)
        game.drawText("ESC to quit / SPACE to continue",250,150,white)
        game.update(60)

def draw():
    bk.draw()
    for x in range(len(pipes)):
        pipes[x].move()
        if pipes[x].isOffScreen():
            pipes[x].reset()
    bar.draw() 

def checkcollision():
    for x in range(len(pipes)):
        if bird.graphics.collidedWith(pipes[x].pipeTOP,"rectangular") or \
        bird.graphics.collidedWith(pipes[x].pipeBOT,"rectangular"):
            hit.play()
            game.over = True

        #Pass the right side of the top pipe
        if pipes[x].pipeTOP.right <= bird.graphics.left and not pipes[x].passed:
            game.score += 1
            point.play()
            pipes[x].passed = True
            score_one.nextFrame()
            if game.score%10 == 0:
                score_one.moveTo(362,455)
                score_ten.visible = True
                score_ten.moveTo(337,455)
                score_ten.nextFrame()
                
            
    if bird.graphics.y > game.top and bird.graphics.y < bar.top:  
        if keys.Pressed[K_SPACE]:
            bird.move()
        else:
            bird.fly()
    else:
        game.over = True

#Game Loop
while not quit:
    game.processInput()
    startscreen()
    #Main Loop
    while not game.over:
        game.processInput()
        draw()
        checkcollision()
        score_one.draw()
        score_ten.draw()
        game.update(60)
    #End Main Loop
    clearpipes()
    game.update(60)
#End Game Loop
            
game.quit()
