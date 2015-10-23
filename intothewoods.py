from time import sleep
import os
import json
import sys
import random
import terminalsize

last = 0

def slowPrint(line, delay=0.03):
	for i in range(0, len(line)):
		print(line[i], end="")
		sys.stdout.flush()
		sleep(delay)
	print()

def clearScreen():
	sys.stdout.write("\x1b[2J\x1b[H")
	sys.stdout.flush()

def delayPrint(line, delay=1):
	sleep(delay)
	slowPrint(line)

def delayLine(delay=1):
	sleep(delay)
	print()

def clearLastLine():
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K' #or 1k?
	print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
	print()

def clearLastLineNoNewline():
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K' #or 1k?
	print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

def choice(num):
	global last

	fc = json.load(open(os.path.join(startDir, tree[num]), "r"))
	node = fc[num]
	if node.get("S") != None:
		if type(node.get("S")) is list:
			ridx = random.randrange(0, len(node["S"]))
			delayPrint(node["S"][ridx])
		else:
			delayPrint(node["S"])
		print()
		input("-> Press Enter to Continue <-".center(terminalsize.get_terminal_size()[0]))
		clearLastLine()
		clearScreen()

	if node.get("Q") == None:
		if node["N"] == -1:
			delayPrint("[!] You have died! Game over!")
			sleep(1.5)
			return
		if node["N"] == -2:
			delayPrint("YOU WIN! YOU SURVIVED THE TERRIBLE FOREST!")
			sleep(1.5)
			return
		if node["N"] == -3:
			choice(last)
			return
		choice(node["N"])
		return

	options = node["R"]
	delayPrint("[?] " + node["Q"])

	inc = 0
	nexts = []
	statements = []
	for option in options:
		delayPrint("\t{}: {}".format(inc, option), 0.75)
		inc = inc + 1
		nexts.append(options[option])
		statements.append(option)
	sleep(0.75)
	while True:
		try:
			c = int(input("Choice: "))
			if c >= inc:
				raise ValueError
			picked = statements[c]
			last = num
		except ValueError:
			print("Please enter a valid choice!")
			sleep(1)
			clearLastLineNoNewline()
			clearLastLineNoNewline()
		else:
			break
	delayLine()
	delayPrint("==> " + picked)
	delayLine()
	choice(nexts[c])

def titleSequence():
	print()
	delayPrint("\x1b[1m" + " Into the Woods ".center(terminalsize.get_terminal_size()[0]) + "\x1b[0m")
	delayLine()
	delayPrint("A game made by Layne Gustafson".center(terminalsize.get_terminal_size()[0]))
	delayLine()
	print("\x1b[5m", end="")
	input("-> Press enter to start <-".center(terminalsize.get_terminal_size()[0]))
	print("\x1b[0m", end="")
	clearScreen()

tree = {}

startDir = os.path.join(os.getcwd(), "story")

for storyFile in os.listdir(startDir):
	info = json.load(open(os.path.join(startDir, storyFile), "r"))
	for key in info:
		tree[key] = storyFile


clearScreen()
titleSequence()

choice("0")