import requests
import random

def generate(req_count):
	results = []
	for i in range(req_count):
		name = None
		response = requests.get("https://random-word-api.herokuapp.com/word")
		word = response.json()[0]
		chance = random.randrange(0, 2)
		if chance == 1:
			number = random.randrange(1,1001)
			name = f"{word}{number}"
		else:
			name = f"{word}"
		results.append(name)
	return results



if __name__ == '__main__':
	
	usernames = generate(25)
	with open('usernames.txt', 'w') as FILE:
		for usr in usernames:
			FILE.write(f"{usr}\n")
