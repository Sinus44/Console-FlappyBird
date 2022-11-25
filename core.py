import os
import time
import keyboard
import subprocess
import threading
import timeit
import pyaudio
import wave
import ctypes
import datetime

class Color:

    BLACK    = '\33[30m'
    RED      = '\33[31m'
    GREEN    = '\33[32m'
    YELLOW   = '\33[33m'
    BLUE     = '\33[34m'
    PURPLE   = '\33[35m'
    SKY      = '\33[36m'
    SNOW     = '\33[37m'
    GREY     = '\33[90m'
    PINK     = '\33[91m'
    LIME     = '\33[92m'
    BANANA   = '\33[93m'
    AZURE    = '\33[94m'
    VIOLET   = '\33[95m'
    AQUA     = '\33[96m'
    WHITE    = '\33[97m'

    class Background:
        BLACK  = '\33[40m'
        RED    = '\33[41m'
        GREEN  = '\33[42m'
        YELLOW = '\33[43m'
        BLUE   = '\33[44m'
        PURPLE = '\33[45m'
        SKY    = '\33[46m'
        SNOW   = '\33[47m'
        GREY   = '\33[100m'
        PINK   = '\33[101m'
        LIME   = '\33[102m'
        BANANA = '\33[103m'
        AZURE  = '\33[104m'
        VIOLET = '\33[105m'
        AQUA   = '\33[106m'
        WHITE  = '\33[107m'

    class Style:
        END      = '\33[0m'
        ITALIC   = '\33[3m'
        URL      = '\33[4m'
        SELECTED = '\33[7m'

    def init(fast=True):
        if fast:
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11),7)
        else:
            os.system("")


    def example():
        print(Color.BLACK +"BLACK")
        print(Color.GREY  +"GREY")
        print(Color.SNOW  +"SHOW")
        print(Color.WHITE +"WHITE")

        print(Color.RED   +"RED")
        print(Color.PINK  +"PINK")

        print(Color.GREEN +"GREEN")
        print(Color.LIME  +"LIME")

        print(Color.YELLOW+"YELLOW")
        print(Color.BANANA+"BANANA")

        print(Color.BLUE  +"BLUE")
        print(Color.AZURE +"AZURE")
        print(Color.SKY   +"SKY")
        print(Color.AQUA  +"AQUA")

        print(Color.PURPLE+"PURPURE")
        print(Color.VIOLET+"VIOLET")

class Window:
	buffer = []
	w = 0
	h = 0

	def __init__(self, w=10, h=10):
		self.w = w
		self.h = h

	def draw(self, fast=True):
		if not fast:
			for i in self.buffer:
				print("".join(i))
		else:
			s=""
			for i in self.buffer:
				s+="".join(i)+"\n"
			s = bytes(s,"utf-8")
			os.write(1,s)

	def clear(self, fast=True):
		if fast: print("\033[J")
		else: os.system("cls")

	def fill(self, symbol=" "):
		self.buffer = []
		for i in range(self.h):
			self.buffer.append([])
			for j in range(self.w):
				self.buffer[i].append(symbol)

	def point(self, x=0, y=0, symbol="*"):
		if 0 <= x < len(self.buffer[0]):
			if 0 <= y < len(self.buffer):
				self.buffer[y][x] = symbol

	def rectFill(self, x=0, y=0, w=1, h=1, symbol="*"):
		for i in range(self.h):
			for j in range(self.w):
				if (y <= i <= y+h-1) and (x <= j <= x+w-1):
					self.buffer[i][j] = symbol

	def circleFill(self, x=0, y=0, r=1, symbol="*"):
		for i in range(self.h):
			for j in range(self.w):
				if (i-y)**2 + (j-x)**2 <= r**2:
					self.buffer[i][j] = symbol

	def line(self, x1=0, y1=0, x2=0, y2=0, symbol="*"):
		delX = abs(x2 - x1)
		delY = abs(y2 - y1)

		signX, signY = 0, 0

		if x1 < x2: signX = 1
		else: signX = -1

		if y1 < y2: signY = 1
		else: signY = -1

		error = delX - delY

		while (x1 != x2 or y1 != y2): 
			self.point(x1, y1, symbol)
			error_2 = error * 2
        
			if error_2 > -delY: 
				error -= delY
				x1 += signX
        
			if error_2 < delX:
				error += delX
				y1 += signY

	def paste(self, frame, x=0, y=0):
		if x+frame.w > self.w or y+frame.h > self.h:
			print("ERROR")
			return

		for i in range(frame.h):
			for j in range(frame.w):
				self.buffer[i+y][j+x] = frame.buffer[i][j]

	def text(self, text="TEXT", x=0, y=0, color=Color.WHITE, backgroundColor=Color.Background.BLACK):
		if (x<0 or y<0) or (x+len(text) > self.w):
			print("ERROR")
			return

		for i in range(len(text)):
			self.buffer[y][x+i] = color+backgroundColor+text[i]

class Loop:

	def __init__(self, callback, t=1,daemon=False):
		self.on = False
		self.callback = callback
		self.time = t
		self.thread = threading.Thread(target=self.f,daemon=daemon)

	def start(self):
		self.on = True
		self.thread.start()
	
	def f(self):
		while self.on:
			self.callback()
			time.sleep(self.time)

	def stop(self):
		self.on = False	

class Engine:

	def title(title):
		os.system("title "+title)

	def resize(w,h):
		os.system(f'mode con cols={w} lines={h}')

class Keyboard:

	binds = []

	class Bind:
		def __init__(self,type,key,callback):
			self.key = key.upper()
			self.callback = callback
			self.type = type

	def init():
		keyboard.hook(Keyboard.handler)

	def handler(e):
		for i in Keyboard.binds:
			if i.type == e.event_type:
				if i.key == e.name.upper():
					i.callback()

	def addBind(type,key,callback):
		Keyboard.binds.append(Keyboard.Bind(type,key,callback))

class Vector:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

class Mmath:
	def round(x):
		return int((x//1) if x%1<0.5 else ((x//1)+1))

class Performance:
	startTime = 0
	
	def start():
		Performance.startTime = time.time()
	
	def time():
		return time.time() - Performance.startTime

	def function(f,repeats=1,count=1):
		return timeit.repeat(f,repeat=repeats,number=count)


class Sound:
    def __init__(self, filePath):
        self.filePath = filePath
        self.chunksize = 1024
        self.portaudio = pyaudio.PyAudio()

        self.thread = threading.Thread(target=self.p)  
        self.off = False

        self.init()

    def init(self):
        wavefile = wave.open( self.filePath, 'r' )

        self.format = self.portaudio.get_format_from_width(wavefile.getsampwidth())
        self.channels = wavefile.getnchannels()
        self.rate = wavefile.getframerate()

    def p(self):
        wavefile = wave.open( self.filePath, 'r' )

        self.streamobject = self.portaudio.open(format = self.format, channels = self.channels, rate = self.rate, output = True ) 
        self.data = wavefile.readframes(self.chunksize)

        while len(self.data) > 0 and not self.off:
            if self.off: return
            self.streamobject.write(self.data)
            self.data = wavefile.readframes(self.chunksize)

    def play(self):
        self.off = False
        if not self.thread.is_alive():
            self.thread = threading.Thread(target=self.p)
            self.thread.start()

    def stop(self):
        self.off = True

class Logging:
	def log(*text):
		date = datetime.datetime.now()
		file = open(f"{date.day}{date.month}{date.year}.log","a")

		for i in text:
			file.write(f"[{'{:2.0f}'.format(date.hour)}:{'{:2.0f}'.format(date.minute)}:{'{:2.0f}'.format(date.second)}]: {str(i)}\n")

		file.close()