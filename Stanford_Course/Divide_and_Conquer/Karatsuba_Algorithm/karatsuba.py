#!/usr/bin/python2.7.11
numbers_file = open('numbers.txt', 'r')
lines = [int(i) for i in numbers_file.read().split()]

for i in lines:
	print i, type(i)
