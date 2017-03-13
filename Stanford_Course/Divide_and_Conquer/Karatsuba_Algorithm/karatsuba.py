#!/usr/bin/python2.7.11
numbers_file = open('numbers.txt', 'r')
lines = numbers_file.read().split()
number_string = 'number_'
list_of_numbers = [number_string + str(i) for i in range(1, len(lines) + 1)]

print list_of_numbers


