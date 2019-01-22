#!/usr/bin/python3
import random #for randomizing lists
import time

def read_file():
	f = open('jobs.txt', 'r')
	if f:
		print("file read!")
		lines = f.readlines()
		num_jobs = int(lines[0])
		lines = lines[1:]
		lines = [(int(line.split()[0]), int(line.split()[1]), int(line.split()[0]) - int(line.split()[1])) for line in lines]
		f.close()
		return num_jobs, lines
	else:
		f.close()

def merge_sort(given_list):
	"""This method runs merge
	sorting calls on several
	defined functions."""

	merged_array = []

	if len(given_list) == 0: #base case for empty list
		return [] #must return empty, otherwise get error
	if len(given_list) == 1: #base case for when list is one length, key point
		return given_list
	if len(given_list) > 0: #base case for divide and conquer
		on_the_left = merge_sort(left_list(given_list))
		on_the_right = merge_sort(right_list(given_list))
		merged_array = ascending_order(on_the_left, on_the_right)
	return merged_array

def left_list(given_list):
	"""Creates left list by contiually
	dividing input list by two. This
	method does first half of the given
	array."""
	if int(len(given_list) / 2) > 0:
		return given_list[:int(len(given_list) / 2)]
	else:
		return []

def right_list(given_list):
	"""Creates left list by contiually
	dividing input list by two. This
	method does second half of the give
	array."""
	if int(len(given_list) / 2) > 0:
		return given_list[int(len(given_list) / 2):]
	else:
		return []			

def ascending_order(left_array, right_array):
	"""This method sorts the array by
	ascending order."""
	ordered_array = []

	if left_array:
		left_size = len(left_array)
	else: #need to hard code zero length for empty list because of error message
		left_size = 0
	if right_array:
		right_size = len(right_array)
	else: #need to hard code zero length for empty list because of error message
		right_size = 0

	i = 0
	j = 0

	while(i < left_size and j < right_size): #indices run until out of bounds
		if left_array[i][2] > right_array[j][2]:
			ordered_array.append(right_array[j])
			j += 1
		elif left_array[i][2] < right_array[j][2]:
			ordered_array.append(left_array[i])
			i += 1
		else:
			print(left_array[i], right_array[j])
			if left_array[i][0] < right_array[j][0]:
				ordered_array.append(right_array[j])
				ordered_array.append(left_array[i])
				i += 1
				j += 1
			else:
				ordered_array.append(left_array[i])
				ordered_array.append(right_array[j])
				i += 1
				j += 1

	while i < left_size: #activates if one of the lists goes through its elements soon
		ordered_array.append(left_array[i])
		i += 1
	while j < right_size: #activates if one of the lists goes through its elements soon
		ordered_array.append(right_array[j])
		j += 1
	return ordered_array

if __name__ == "__main__":
	high = 76
	start = time.time()
	num_jobs, weights_lengths = read_file()
	print(weights_lengths[:high])
	sorted_array = merge_sort(weights_lengths[:high])
	end = time.time()
	print("xxxxxxxxxxxx",sorted_array)
	print("run time:", end - start)

"""This file describes a set of jobs with positive and
integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59",
indicating that the second job has weight 74 and
length 59.

You should NOT assume that edge weights or lengths are
distinct.

Your task in this problem is to run the greedy algorithm
that schedules jobs in decreasing order of the difference
(weight - length). Recall from lecture that this
algorithm is not always optimal. IMPORTANT: if two jobs
have equal difference (weight - length), you should schedule
the job with higher weight first. Beware: if you break ties
in a different way, you are likely to get the wrong answer.
You should report the sum of weighted completion times of
the resulting schedule --- a positive integer --- in the
box below.

ADVICE: If you get the wrong answer, try out some small
test cases to debug your algorithm (and post your test
	cases to the discussion forum)."""