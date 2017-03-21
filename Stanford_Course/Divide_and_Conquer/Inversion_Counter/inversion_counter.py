if __name__ == "__main__":
	numbers_file = open('integerArray.txt', 'r')
	lines = [int(i) for i in numbers_file.read().split()]
	for i in lines:
		print i
	numbers_file.close()