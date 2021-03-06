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
	for line in list_of_tuples:
		temp = line.split()
		new_list.append((int(temp[0]), int(temp[1]), int(temp[2])))
	return new_list

def create_graph(list_of_tuples):
	graph = {}
	for i in list_of_tuples:
		if i[0] not in graph:
			graph[i[0]] = []
			graph[i[0]].append(i)
			graph[i[0]].append((i[1], i[0], i[2]))
		else:
			graph[i[0]].append(i)
			graph[i[0]].append((i[1], i[0], i[2]))
		if i[1] not in graph:
			graph[i[1]] = []
			graph[i[1]].append(i)
			graph[i[1]].append((i[1], i[0], i[2]))
		else:
			graph[i[1]].append(i)
			graph[i[1]].append((i[1], i[0], i[2]))
	return graph

def primm_algorithm(graph, starting_node):
	seen = []
	not_seen = list(graph.keys())
	queue = []
	min_span_tree = []
	detritus = set()
	holder = []

	while not_seen:
		seen.append(starting_node)
		not_seen.remove(starting_node)
		queue = update_queue(graph, starting_node, seen, queue, detritus)
		min_edge = min_tuple(starting_node, seen, queue)
		if not min_edge:
			seen.sort()
			if seen == list(range(1,501)):
				print("all nodes seen")
			return min_span_tree
		if min_edge not in holder:
			holder.append(min_edge)
			holder.append((min_edge[1], min_edge[0], min_edge[2]))
		detritus = set(holder)
		queue = clean_up(queue, detritus)
		starting_node = new_start(min_edge, seen, queue)
		min_span_tree.append(min_edge)

def update_queue(graph, starting_node, seen, queue, detritus):
	for i in graph[starting_node]:
		if i not in queue:
			queue.append(i)
	return sorted(list(set(queue) - detritus), key = by_third)

def min_tuple(starting_node, seen, queue):
	for i in queue:
		if i[0] not in seen:
			return i
		if i[1] not in seen:
			return i

def clean_up(queue, detritus):
	return sorted(list(set(queue) - detritus), key = by_third)

def new_start(min_edge, seen, queue):
	if min_edge[1] not in seen:
		return min_edge[1]
	if min_edge[0] not in seen:
		return min_edge[0]

def by_third(item):
	return item[2]

def length_now(tuple_passed, length_so_far):
	return length_so_far + tuple_passed[1]

if __name__ == "__main__":
	#master_cost()
	###################
	nodes, edges, graph = read_file_graph()
	for i in range(0, 10):
		random.seed(a = i)
		starting_node = random.choice(list(graph.keys()))
		print("xxxxxxxxxxxxxxxx")
		print("seed:", i)
		print("starting_node:", starting_node)
		min_span_tree = primm_algorithm(graph, starting_node)
		print("length of min_span_tree:", len(set(min_span_tree)))
		sum = 0
		for i in min_span_tree:
			sum += i[2]
		print(sum)

#69119377652
#67311454237
#-3612829