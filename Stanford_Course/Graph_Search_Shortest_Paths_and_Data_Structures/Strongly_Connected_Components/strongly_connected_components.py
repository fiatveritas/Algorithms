#!/usr/bin/python2.7

# Kosaraju's Algorithm

#first and foremost I have to
#thank a fellow githuber some 
#of the solution is in part
#his/hers. My solution had 
#the right spirit.

import sys, resource, time

# Increase recursion limit and stack size
# Stuff won't finishing running otherwise

sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit, hardlimit))


# n - Number of nodes
# This assignment needs to be explict
# I tried solving this without defining
# this globally and it was a headache

n = 875714 

def Kosaraju(Graphed, Graphed_reversed):
    """This method implements other function defined on this file. 
    Moreover, there are global assignments which I discuss below."""
    

    # leader keeps track of what the source node is
    # finish gives finishing time when starting at that node

    global leader, finish

    leader = {}
    finish = {}

    # Run first DFS Loop, returns list of finish times
    DFS_Loop(Graphed_reversed)

    # Reorder graph with nodes numbered according to finish time
    Graphed_reordered = {}
    g_values = Graphed.values()
    for i in range(1, n+1):
        temp = g_values[i-1]
        Graphed_reordered[finish[i]] = [finish[x] for x in temp]

    # Run second DFS Loop with reordered graph
    DFS_Loop(Graphed_reordered)

    return leader

def DFS_Loop(Graphed):
    global t, s, seen
    t = 0 # Number of nodes processed, good for recursion assigns runtime
    s = 0 # Current source vertex, good for backtrack or knowing path

    # Initialize all nodes as unexplored
    seen = {}
    for node in range(1, n+1):
        seen[node] = 0 

    # Explore each adjacent node i (if unexplored)
    for node in range(n, 0, -1):
        if seen[node] == 0:
            s = node
            DFS(Graphed, node)

def DFS(Graphed, node):
    # Run Depth First Search
    global t
    seen[node] = 1 # Mark node i as explored. node is passed in from DFS_Loop or recursion.
    leader[node] = s # Sets leader as node s, helps track path

    # exploration by depth
    for j in Graphed[node]:
        if seen[j] == 0:
            DFS(Graphed, j)
    t += 1
    finish[node] = t
   
def get_graph():
    """This methods pulls nodes from input file and maps each node to another node."""
    Graphed, Graphed_reversed = {}, {}
    for i in range(1, n+1):
        Graphed[i], Graphed_reversed[i]  = [], []

    # Create structure of graph.
    file = open('SCC.txt')
    for line in file:
        list = line.split()
        i = int(list[0])
        j = int(list[1])
        Graphed[i].append(j)
        Graphed_reversed[j].append(i)
    file.close()

    return Graphed, Graphed_reversed

def most_common(list_of_stuff, n_most_common):
    """This method return the n_most_common nodes"""
    from collections import Counter

    c = Counter(list_of_stuff)
    result = []

    for number, count in c.most_common(n_most_common):
        result.append(count)
    
    return result

if __name__=="__main__":
    start = time.time()
    Graphed, Graphed_reversed = get_graph()
    print "Graph grabbed in", time.time() - start,"seconds"

    start = time.time()
    leader = Kosaraju(Graphed, Graphed_reversed)
    print "Kosaraju's Algorithm ran in", time.time() - start,"seconds"

    print "Size of the top 5 strongly connected components:"
    print most_common(leader.values(), 5)