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



def quicksort(to_be_sorted):
	"""this method sorts an array of unique positive numbers using
	the quicksort algorithm using the last element as a pivot."""
	if len(to_be_sorted) == 0:
		return []
	if len(to_be_sorted) == 1:
		return to_be_sorted
	if len(to_be_sorted) > 1:
		i = 0
		j = 0
		upper_limit = len(to_be_sorted)
		print(to_be_sorted)
		while j < upper_limit - 1:
			if i == j and to_be_sorted[j][2] < to_be_sorted[upper_limit -1][2]:
				print(to_be_sorted[j][2], "vs", to_be_sorted[upper_limit -1][2])
				i += 1
				j += 1
			elif to_be_sorted[j][2] > to_be_sorted[upper_limit -1][2]:
				print(to_be_sorted[j][2], "vs", to_be_sorted[upper_limit -1][2])
				j += 1
			elif to_be_sorted[j][2] < to_be_sorted[upper_limit -1][2]: # [49, 97, 53, 5, 33, 65, 62, 51, 38, 61]
			    print(to_be_sorted[j][2], "vs", to_be_sorted[upper_limit -1][2])
			    to_be_sorted[i], to_be_sorted[j] = swap(to_be_sorted[i], to_be_sorted[j])
			    i += 1
			    j += 1
	to_be_sorted[i], to_be_sorted[upper_limit -1] = swap(to_be_sorted[i], to_be_sorted[upper_limit -1])
	to_be_sorted[:i] = quicksort(to_be_sorted[:i])
	to_be_sorted[i:] = quicksort(to_be_sorted[i:])
	print(to_be_sorted)
	return to_be_sorted


def swap(element_1, element_2):
	"""this method swaps two elements passed into the function"""
	holder = element_1
	element_1 = element_2
	element_2 = holder
	return element_1, element_2

if __name__ == "__main__":
	start = time.time()
	num_jobs, weights_lengths = read_file()
	sorted_array = quicksort(weights_lengths[:11])
	end = time.time()
	print(sorted_array)
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