#!/usr/bin/python2.7.11
import numpy as np
def divider(number, counter = 0):
	if number / 10 < 10:
		counter += 1
		return (number / 10, counter)
	elif number / 10 >= 10:
		counter += 1
		return divider(number / 10, counter = counter)
def karatsuba(x, y):
	#print x, y
	if (x < 10) or (y < 10):
		return x * y
	elif (x >= 10) and (y >= 10):
		length = max(len(str(x)), len(str(y)))
		div_by_2 = length / 2

		x1 = x / (10 **(div_by_2))
		x0 = x % (10 **(div_by_2))
		#print str(x), '=', str(x_1), '* 2^', str(m), '+',str(x_0)
		y1 = y / (10 **(div_by_2))
		y0 = y % (10 **(div_by_2))
		#print str(y), '=', str(y_1), '* 2^', str(m), '+',str(y_0)
		z2 = x1 * y1
		z0 = karatsuba(x0, y0)
		z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0
	return z2*10**(2*div_by_2) + z1*10**div_by_2 + z0

if __name__ == '__main__':
	numbers_file = open('numbers.txt', 'r')
	lines = [int(i) for i in numbers_file.read().split()]
	number_1 = lines[0]
	number_2 = lines[1]
	print number_1
	print number_2
	print karatsuba(x = number_1, y = number_2)
	