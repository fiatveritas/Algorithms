#!/usr/bin/python2.7.11
def divider(number, counter = 0):
	if number / 10 < 10:
		counter += 1
		return (number / 10, counter)
	elif number / 10 >= 10:
		counter += 1
		return divider(number / 10, counter = counter)
def karatsuba(x, y):
	x_1, m = divider(number = x)
	x_0 = x - x_1 * 10**m
	print str(x), '=', str(x_1), '* 10^', str(m), '+',str(x_0)

	y_1, m = divider(number = y)
	y_0 = y - y_1 * 10**m
	print str(y), '=', str(y_1), '* 10^', str(m), '+',str(y_0)	
	return None
if __name__ == '__main__':
	numbers_file = open('numbers.txt', 'r')
	lines = [int(i) for i in numbers_file.read().split()]
	number_1 = lines[0]
	number_2 = lines[1]
	karatsuba(x = number_1, y = number_2)