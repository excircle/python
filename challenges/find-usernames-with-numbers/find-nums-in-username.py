if __name__ == '__main__':
	with open('usernames.txt', 'r') as FILE:
		users_with_numbers = []
		for name in FILE.read().splitlines():
			digit_analysis = [char.isdigit() for char in name]
			if True in set(digit_analysis):
				users_with_numbers.append(name)
		print(users_with_numbers)
		print(len(users_with_numbers))