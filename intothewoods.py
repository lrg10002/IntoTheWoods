from time import sleep

last = 0

def choice(num):
	global last

	print()
	if tree[num].get("Statement") != None:
		print(tree[num]["Statement"])
		input("-> Press Enter to Continue <-")
		sleep(1)
		print()

	if tree[num].get("Question") == None:
		if tree[num]["Next"] == -1:
			sleep(1)
			print("[!] You have died! Game over!")
			sleep(1.5)
			return
		if tree[num]["Next"] == -2:
			sleep(1)
			print("YOU WIN! YOU SURVIVED THE TERRIBLE FOREST!")
			sleep(1.5)
			return
		if tree[num]["Next"] == -3:
			choice(last)
			return
		choice(tree[num]["Next"])
		return

	options = tree[num]["Responses"]
	sleep(1)
	print("[?] " + tree[num]["Question"])

	inc = 0
	nexts = []
	statements = []
	for option in options:
		sleep(0.75)
		print("\t{}: {}".format(inc, option))
		inc = inc + 1
		nexts.append(options[option])
		statements.append(option)
	while True:
		try:
			c = int(input("Choice: "))
			if c >= inc:
				raise ValueError
			picked = statements[c]
			last = num
		except ValueError:
			print("Please enter a valid choice!")
		else:
			break
	sleep(1)
	print()
	sleep(1)
	print("==> " + picked)
	sleep(1)
	choice(nexts[c])


tree = {
	"shutup": {
		"Statement": "Oh, just shut up!", #todo: implement multiple random statements
		"Next": -3
	},

	0: {
		"Question": "You are walking through the forest when you trip on a sleeping bear. What do you do?",
		"Responses": {"Eat the bear":"eatbear", "Caress the bear":"caressbear", "Chew the bear":"chewbear"}
	},
	"eatbear": {
		"Statement": "Before you can eat the bear, the bear eats you!",
		"Next": -1
	},
	"caressbear": {
		"Statement": "The bear wakes up to the gentle touch of your strong yet supple hands. He enjoys it immensely.",
		"Question": "What do you do to the bear next?",
		"Responses": {
			"Eat the bear": "eatbear", 
			"Engage in rompus crossfit training with the bear": "crossfitbear", 
			"Share your fruitsnacks with the bear": "fruitsnacksbear"
		}
	},
	"crossfitbear": {
		"Statement": "The bear, having just been awakened, is in no mood for crossfit and decapitates you.",
		"Next": -1
	},
	"fruitsnacksbear": {
		"Statement": "The bear greatly enjoys your fruitsnacks. He eats all of them.",
		"Next": -2
	},
	"chewbear": {
		"Statement": "Suprisingly, the bear enjoys the sensation of your teeth gnawing at his gnarly coat.",
		"Question": "What's next? You can't possibly chew on the bear forever!",
		"Responses": {
			"Or can you?": "shutup",
			"Keep chewing, just for one minute longer": "chewbearlonger",
			"Recite to the bear your impersonation of President Clinton's 1997 State of the Union Address": "stateoftheunionbear"
		}
	},
	"chewlonger": {
		"Statement": "You chew for one minute longer.",
		"Question": "Now what do you do?",
		"Responses": {
			"Chew even more": "jawfallsoffbear"
		}
	},
	"jawfallsoffbear": {
		"Statement": "You chew so much that your jaw falls off your face.",
		"Next": -1
	},
	"stateoftheunionbear": {
		"Statement": "You: \"Mr. Speaker, Mr. Vice President, members of the 105th Congress, distinguished guests, my fellow Americans: I think I should start by saying thanks for inviting me back.\"\nBear: \"...\"\nYou: \"I come before you tonight with a challenge as great as any in our peacetime history – and a plan of action to meet that challenge, to prepare our people for the bold new world of the 21st century.\"\nBear: \"What is this shit?!\"\nYou: \"...\"",
		"Next": "bearpunts"
	},
	"bearpunts": {
		"Statement": "The bear punts you to China.",
		"Next": -1
	}
}

choice(0)