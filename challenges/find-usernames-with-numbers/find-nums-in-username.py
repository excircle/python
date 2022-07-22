if __name__ == '__main__':
	with open('usernames.txt', 'r') as FILE:
		users_with_numbers = []
		for name in FILE.read().splitlines():
			split_list = list(name)
			for char in split_list:
				if char.isdigit():
					users_with_numbers.append(name)
					break
				else:
					pass
		print(users_with_numbers)
		print(len(users_with_numbers))