import os, json

story_dir = os.path.join(os.getcwd(), "story")

targets = {}
missing = []

for story_file in os.listdir(story_dir):
	info = json.load(open(os.path.join(story_dir, story_file), "r"))
	for key in info:
		targets[key] = story_file
for story_file in os.listdir(story_dir):
	info = json.load(open(os.path.join(story_dir, story_file), "r"))
	for key in info:
		if info[key].get("R") == None:
			continue
		for goto_key in info[key]["R"].values():
			if targets.get(goto_key) == None:
				missing.append(goto_key)

for x in missing: print(x)