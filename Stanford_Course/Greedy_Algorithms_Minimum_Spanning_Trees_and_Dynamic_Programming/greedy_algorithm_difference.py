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

def by_diff(item):
	return item[2]
def by_weight(item):
	return item[0]

if __name__ == "__main__":
	high = 10000
	start = time.time()
	num_jobs, weights_lengths = read_file()
	#sorted_array = merge_sort(weights_lengths[:high])
	sorted_array = sorted(sorted(weights_lengths, key = by_weight, reverse = True), key = by_diff)
	end = time.time()
	#print(weights_lengths[:high])
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