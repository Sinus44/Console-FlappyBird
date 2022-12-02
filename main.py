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

god = False

debug = "Kek"

menu = None
title = "Flappy Bird by Sinus44"

def setup():
	global window, drawing, logicing, jumpSound, backSound, backgroundSound, maxPipes, W, H, pipesDistance, menu
	Engine.title("Loading...")
	Color.init()
	Keyboard.init()
	Engine.resize(W, H+1)
	window = Window(W, H)

	Keyboard.addBind("down", "esc", exitGame)
	Keyboard.addBind("down", "space", jump)
	Keyboard.addBind("down", "g", godmode)
	Keyboard.addBind("down", "w", move, "up")
	Keyboard.addBind("down", "s", move, "down")

	jumpSound = Sound("./assets/sounds/jump.wav")
	backgroundSound = Sound("./assets/sounds/background.wav")

	maxPipes = ( W // pipesDistance )+1

	drawing = Loop(draw, 1/60) # 60 FPS
	drawing.start()

	logicing = Loop(logic, 1/10)
	logicing.start()

	backSound = Loop(playBack, 40)
	backSound.start()

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
	global window, offset, pipes, player, W, H, pipesDistance, counter, pipesWidth, debug, free, color
	window.fill(Color.Background.SKY+" ")

	for i in range(len(pipes)):
		window.rectFill( W - ( i * pipesDistance + offset )-1, 0, pipesWidth, pipes[i], Color.Background.LIME+" ")
		window.rectFill( W - ( i * pipesDistance + offset )-1, pipes[i]+free, pipesWidth, H - pipes[i]-free, Color.Background.LIME+" ")
	window.point(player[0], player[1], Color.BANANA+"O")
	window.text(str(counter), W-len(str(counter))-5,2,Color.BLACK + Color.Background.SKY)
	window.draw(True)

def logic():
	global offset, maxPipes, pipes, player, W, H, pipesDistance, pipesWidth, debug, free, god
	if not god: 
		player[1] += 1 if player[1]+1 < H else H - player[1] - 1

	if offset>=pipesDistance:
		addPipe()
		offset = 0
	offset += 1
	lastPipeX = W - ((len(pipes)-1) * pipesDistance + offset) 

	if (player[0] >= lastPipeX-1) and (player[0] < lastPipeX+pipesWidth):
		if len(pipes)>0:
			lastPipeY = pipes[-1]
			if (player[1]<lastPipeY) or (player[1]>=lastPipeY+free):
				gameEnd()

def gameEnd():
	menuInit()

def exitGame():
	global  drawing, logicing, jumpSound, backSound, backgroundSound, W, H, counter

	# Threads:
	if logicing: logicing.stop()
	if drawing: drawing.stop()
	if reDraw: reDraw.stop()
	if backSound: backSound.stop()
	if jumpSound: jumpSound.stop()

	#Sounds:
	if backgroundSound: backgroundSound.stop()
	if jumpSound: jumpSound.stop()

	#Keyboard:
	Keyboard.stop()
	Keyboard.reset()

	quit()

def godmode():
	global god
	god = not god

def move(orientation):
	if god:
		if orientation == "up":
			player[1] -= 1
		elif orientation == "down":
			player[1] += 1

setup()