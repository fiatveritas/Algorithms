
# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 6 - Part 1
# Count number of 2 sum variations where x + y = t
# t is any integer in interval [-10000, 10000]
# Hash table utilization problem

import urllib2


f = open('2_Sum.txt', 'r')
lines = f.readlines()
f.close()
lines = [int(line) for line in lines]

for i in range(20):
    print lines[i], type(lines[i])