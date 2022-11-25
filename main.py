from core import *
from random import randint,choice

window = None
drawing = None
logicing = None
jumpSound = None
backSound = None
backgroundSound = None

offset = 0
maxPipes = 0

pipes = []
player = [2,8]

W = 120
H = 30
pipesDistance = 31 # 1 - каждый символ при ширине 1 px
pipesWidth = 2
counter = 0

free = 5

x = "Kek"

def setup():
	global window, drawing, logicing, jumpSound, backSound, backgroundSound, maxPipes, W, H, pipesDistance
	Engine.title("Loading...")
	Logging.log("Game loading...")

	Color.init()
	Keyboard.init()

	Engine.resize(W, H)

	window = Window(W, H)

	Keyboard.addBind("down", "esc", stopGame)
	Keyboard.addBind("down", "space", jump)

	jumpSound = Sound("./assets/sounds/jump.wav")
	backgroundSound = Sound("./assets/sounds/background.wav")

	maxPipes = ( W // pipesDistance )+1

	Engine.title("Flappy Bird")

	drawing = Loop(draw, 1/60) # 60 FPS
	drawing.start()

	logicing = Loop(logic,1/10)
	logicing.start()

	backSound = Loop(playBack,40)
	backSound.start()

	Logging.log("Loaded")

def playBack():
	global backgroundSound
	backgroundSound.play()

def addPipe():
	global maxPipes, pipes, H, counter
	if len(pipes) >= maxPipes:
		pipes.pop(-1)
		counter+=1
	pipes.insert(0,randint(0,H-1))

def jump():
	global jumpSound, offset, player
	player[1] -= 3 if player[1]-3>0 else player[1]
	jumpSound.play()

def draw():
	global window, offset, pipes, player, W, H, pipesDistance, counter, pipesWidth, debug, free
	window.fill(Color.Background.SKY+" ")

	for i in range(len(pipes)):
		window.rectFill( W - ( i * pipesDistance + offset ), 0, pipesWidth, pipes[i],  Color.LIME+Color.Background.LIME+"*")
		window.rectFill( W - ( i * pipesDistance + offset ), pipes[i]+free, pipesWidth, H - pipes[i], Color.LIME+Color.Background.LIME+"*")

	window.point(player[0], player[1], Color.BANANA+"O")
	window.text(str(counter), W-len(str(counter))-5,2,Color.BLACK, Color.Background.SKY)
	#window.text(debug, 0, 1, Color.BLACK, Color.Background.SKY)
	window.draw()

def logic():
	global offset, maxPipes, pipes, player, W, H, pipesDistance, pipesWidth, debug, free
	player[1] += 1 if player[1]+1 < H else H - player[1] - 1

	if offset>=pipesDistance:
		addPipe()
		offset = 0
	offset += 1

	lastPipeX = W - ((len(pipes)-1) * pipesDistance + offset) 
	
	if (player[0] >= lastPipeX) and (player[0] < lastPipeX+pipesWidth):
		Logging.log("X Intersection")

		if len(pipes)>0:
			lastPipeY = pipes[-1]
			if (player[1]<lastPipeY) or (player[1]>=lastPipeY+free):
				#debug = "Yes"
				stopGame()
			#else:
				#debug = "No"

def stopGame():
	global  drawing, logicing, jumpSound, backSound, backgroundSound, W, H, counter
	Logging.log("Game stoping...")

	Engine.title("Flappy Bird - The END - Your's score: "+str(counter))
	Logging.log("Preview score")

	backSound.stop()
	Logging.log("Background sound loop off")
	
	backgroundSound.stop()
	Logging.log("Background Sound off")

	jumpSound.stop()
	Logging.log("Jump Sound off")
	
	logicing.stop()
	Logging.log("Logic loop off")
	
	drawing.stop()
	Logging.log("Drawing stop")

	Logging.log("Game stopped")
	quit()

setup()