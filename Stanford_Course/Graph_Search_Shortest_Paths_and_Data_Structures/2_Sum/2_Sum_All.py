#!/usr/bin/python3
import random #for randomizing lists

def sum_2(list_of_numbers, total, look_up_table, pairs_found):
	counter = 0

	for i in list_of_numbers:
		if not look_up_table:
			look_up_table[i] = i
		if total - i not in look_up_table:
			look_up_table[i] = i
		if total - i in look_up_table:
			num_1, num_2 = create_pairs(total - i, i)
			if (num_1, num_2) in pairs_found:
				continue #needed when checking if a pair exists already in hashtable. Again, needed for uniqueness.
			else:
				pairs_found[(num_1, num_2)] = True
				counter += 1
				break #break statement needed to find only one ocurrence. Assignment asked to find if one pair exists, not to find all. Uncomment to find all pairs
	return counter, look_up_table, pairs_found

def create_pairs(num_1, num_2):
	"""this method sorts the pairs in order.
	   needed to check for uniqueness."""
	if num_1 < num_2:
		return num_1, num_2
	elif num_2 < num_1:
		return num_2, num_1
	else:
		return num_1, num_2

def check_algorithm():
	"""this method generates a few randomized
	   lists to test the 2sum algorithm."""
	null_array = []
	array_len_one = [0]

	for i in range(10):
		print("================")
		random.seed(a = i)
		look_up_table = {}
		pairs_found = {}
		test_array = random.sample(range(0, 100), 10)
		num_1, num_2 = random.sample(test_array, 2)
		total = num_1 + num_2
		print("Random list:", test_array)
		print(sum_2(test_array, total, look_up_table, pairs_found)[0], "pair(s) adding to", total)

def read_file():
	"""This method opens the file that contains
	   one-million integers. This file was given
	   by the course masters. Returns a list of
	   integers contained in the file."""
	f = open('2_Sum.txt', 'r')
	lines = f.readlines()
	if lines:
		print("file read!")
	else:
		print("error: problem with file")
	f.close()
	return [int(line) for line in lines]

def run_2sum(list_of_numbers):
	"""This method implements the 2sum algorithm. It determines
	   if each number in the range(-10000, 10001) has pair in 
	   the input file."""
	counter = 0 #counts the number of the relevant range that has a pair in the file
	look_up_table = {} #hashtable for two 2sum
	pairs_found = {} #keeping track of pairs found...needed to check uniqueness
	for t in range(-10000, 10001):
		count, look_up_table, pairs_found = sum_2(list_of_numbers, t, look_up_table, pairs_found) #this funtion tracks the number of ocurrences of pairs for the iterate
		counter += count
	return counter


if __name__ == "__main__":
	list_of_numbers = read_file()
	print(run_2sum(list_of_numbers))
	#check_algorithm() #this line runs the input mentioned above for random lists
	print("================")

	
# Algorithms: Design and Analysis
# Stanford University

# Programming Question
# Count the number of 2-sum variations where x + y = t
# t is any integer in interval [-10000, 10000] inclusive
# Hash table utilization problem

"""
Prompt (verbatim):

The goal of this problem is to implement a variant of
the 2-SUM algorithm covered in this week's lectures.

The file contains 1 million integers, both positive
and negative (there might be some repetitions!).This
is your array of integers, with the ith row 
of the file specifying the ith entry of the array.

Your task is to compute the number of target values
t in the interval [-10000,10000] (inclusive) such 
that there are distinct numbers x,y in the input
file that satisfy x+y=t. (NOTE: ensuring distinctness
requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) 
in the space provided.
"""