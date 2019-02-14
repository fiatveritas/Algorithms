#!/usr/bin/python3
import random #for randomizing lists
import time
import math

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
	return [(int(line.split()[0]), int(line.split()[1]), int(line.split()[0]) - int(line.split()[1]), int(line.split()[0]) / int(line.split()[1])) for line in list_of_interest]

def read_file_weigth_length(lines):
	num_jobs = int(lines[0])
	lines = make_tuples_weight_length(lines[1:])
	return num_jobs, lines
	
def compute_diff_cost(weights_lengths):
	start = time.time()
	sorted_array = sorted(sorted(weights_lengths, key = by_weight, reverse = True), key = by_diff, reverse = True)
	print("diff cost:", weighed_sum(sorted_array))
	end = time.time()
	print("run time:", end - start)

def compute_ratio_cost(weights_lengths):
	start = time.time()
	sorted_array = sorted(sorted(weights_lengths, key = by_weight, reverse = True), key = by_ratio, reverse = True)
	print("ratio cost:", weighed_sum(sorted_array))
	end = time.time()
	print("run time:", end - start)

def by_diff(item):
	return item[2]

def by_weight(item):
	return item[0]

def by_ratio(item):
	return item[3]

def weighed_sum(list_of_interest):
	length_initial = 0
	total_sum = 0
	for i in list_of_interest:
		length_initial = length_now(i, length_initial)
		total_sum += i[0] * length_initial
	return total_sum

def master_cost():
	file_1 = 'jobs.txt'
	lines = open_file(file_1)
	num_jobs, weights_lengths = read_file_weigth_length(lines)
	print("###################")
	print("# of jobs:", num_jobs)
	print("###################")
	compute_diff_cost(weights_lengths)
	print("###################")
	compute_ratio_cost(weights_lengths)

def read_file_graph():
	file_name = 'edges.txt'
	lines = open_file(file_name)
	nodes, edges = int(lines[0].split()[0]), int(lines[0].split()[1])
	lines = create_edges(lines[1:])
	graph = create_graph(lines)
	return nodes, edges, graph

def create_edges(list_of_tuples):
	new_list = []
	reversed_list = []
	for line in list_of_tuples:
		temp = line.split()
		new_list.append((int(temp[0]), int(temp[1]), int(temp[2])))
	return new_list

def create_graph(list_of_tuples):
	graph = {}
	for i in list_of_tuples:
		if i[0] not in graph:
			graph[i[0]] = [i]
			graph[i[0]].append((i[1], i[0], i[2]))
		else:
			graph[i[0]].append(i)
			graph[i[0]].append((i[1], i[0], i[2]))
		if i[1] not in graph:
			graph[i[1]] = [i]
			graph[i[1]].append((i[1], i[0], i[2]))
		else:
			graph[i[1]].append(i)
			graph[i[1]].append((i[1], i[0], i[2]))
	return graph

def primm_algorithm(graph, starting_node, seen, not_seen, queue, min_span_tree):
	while not_seen:
		print("starting_node:", starting_node)
		print("graph[starting_node]:", graph[starting_node])
		seen.append(starting_node)
		not_seen.remove(starting_node)
		queue = queue + graph[starting_node]
		min_edge = min_tuple(queue)
		starting_node = choose_one(min_edge, seen)
		print("================")
		print("min_edge:", min_edge)
		min_span_tree.append(min_edge)
		print("================")
		queue = clean_up(min_edge, queue)
		print("queue clean_up:", queue)
		print("xxxxxxxxxxxxxxxx")
	return min_span_tree

def update_queue(graph, starting_node, seen, queue):
	#
	#
	#
	#

def min_tuple(queue):
	holder = []
	weight = math.inf
	for i in queue:
		if not holder:
			holder.append(i)
			weight = i[2]
		if i[2] < weight:
			holder.clear()
			holder.append(i)
			weight = i[2]
		if i[2] == weight:
			holder.append(i)
	return random.choice(holder)

def choose_one(min_edge, seen):
	if min_edge[0] in seen:
		return min_edge[1]
	elif min_edge[1] in seen:
		return min_edge[0]

def clean_up(min_edge, queue):
	queue.remove(min_edge)
	queue.remove((min_edge[1], min_edge[0], min_edge[2]))
	return queue

def length_now(tuple_passed, length_so_far):
	return length_so_far + tuple_passed[1]

if __name__ == "__main__":
	#master_cost()
	###################
	nodes, edges, graph = read_file_graph()
	random.seed(a = 0)
	starting_node = random.choice(list(graph.keys()))
	seen = []
	not_seen = list(graph.keys())
	queue = []
	min_span_tree = []
	#print("graph:", graph)
	#print("keys:", list(graph.keys()))
	#print("# of nodes:", nodes)
	#print("# of edges", edges)
	print("xxxxxxxxxxxxxxxx")
	min_span_tree = primm_algorithm(graph, starting_node, seen, not_seen, queue, min_span_tree)
	print(min_span_tree)
	#print(len(min_span_tree))
	#sum = 0
	"""for i in min_span_tree:
		sum += i[2]
	print(sum)"""


#random.choice()

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
#69119377652
#67311454237
#

"""This file describes an undirected graph with integer edge
costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874",
indicating that there is an edge connecting vertex #2 and
vertex #3 that has cost -8874. You should NOT assume that
edge costs are positive, nor should you assume that they
are distinct. Your task is to run Prim's minimum spanning
tree algorithm on this graph. You should report the overall
cost of a minimum spanning tree --- an integer, which may
or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the
straightforward O(mn) time implementation of Prim's algorithm
should work fine. OPTIONAL: For those of you seeking an additional
challenge, try implementing a heap-based version. The simpler
approach, which should already give you a healthy speed-up, is
to maintain relevant edges in a heap (with keys = edge costs).
The superior approach stores the unprocessed vertices in the heap,
as described in lecture. Note this requires a heap that supports
deletions, and you'll probably need to maintain some kind of
mapping between vertices and their positions in the heap.

"""