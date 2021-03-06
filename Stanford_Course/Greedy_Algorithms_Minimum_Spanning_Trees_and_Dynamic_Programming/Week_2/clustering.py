#/usr/bin/python3
import random
import time


def open_file(file_name):
	f = open( file_name, 'r')
	if f:
		print("file read!")
		lines = f.readlines()
		f.close()
		return lines
	else:
		f.close()

def make_tuples_weight_length(list_of_interest):
	new_list = []
	for line in list_of_interest:
		temp = line.split()
		new_list.append((int(temp[0]), int(temp[1]), int(temp[2])))
	return new_list

def parse_input():
	edges = open_file("clustering1.txt")
	number_nodes = int(edges[0])
	edges = edges[1:]
	edges = make_tuples_weight_length(edges)
	return number_nodes, edges

def check_cycle(min_span_tree, to_add):
	seen = []
	start = to_add[0]
	print("to_add:", to_add)
	while start not in seen:
		print("****************")
		print("restart while-loop:")
		print("================")
		seen.append(start)
		print("starting node: ", start)
		for i in min_span_tree | set([to_add]):
			print("xxxxxxxxxxxxxxxx")
			print("for-loop:", i)
			if start == i[0] and i[1] not in seen:
				start = i[1]
				break
			elif start == i[0] and i[1] in seen:
				return min_span_tree
	return min_span_tree | set([to_add])

def union_find(min_span_tree, to_add):
	#print("min_span_tree:", min_span_tree)
	#print("edge to_add:", to_add)
	
	return check_cycle(min_span_tree, to_add)

def order_by_weight(item):
	return item[2]


if __name__ == "__main__":
	random.seed(a = 0)
	start_time = time.time()
	min_span_tree = set()
	number_nodes, edges = parse_input()
	edges.sort(key = order_by_weight)

	for i in edges:
		to_add = i
		min_span_tree = union_find(min_span_tree, to_add)
		#break

	#print(edges)
	#print("number_of_edges:", number_nodes)

	"""there = set([(0,1),(1,2),(2,3),(3,4),(4,5)])
	new = (5,0)
	another_new = (5,6)

	print("\n\n\n\nCheck Cycle:\nxxxxxxxxxxxxxxxx")
	print("testing:")
	print(check_cycle(there,new))

	print("\n\n\n\nCheck Cycle:\nxxxxxxxxxxxxxxxx")
	print("testing:")
	print(check_cycle(there,another_new))"""

	print("time_of_execution:", time.time() - start_time)
	print("EOF")

"""In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering.

This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j) for each choice of 1 ≤ i < j ≤n, where n is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
"""

"""
In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is ak -clustering with spacing at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. So you will have to be a little creative to complete this part of the question. For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?
"""