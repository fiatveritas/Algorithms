#!/usr/lib/python3.0
from ast import literal_eval
import numpy as np


class DijkstraPathFinder:

    def __init__(self, input_file):
        self.graph = {}
        with open(input_file) as file:
            for line in file:
                line_content = line.split()
                self.graph[int(line_content[0])] = [literal_eval(edge) for edge in line_content[1:]]
        self._source_vertex = next(iter(self.graph.keys()))

    def compute_shortest_paths(self, source = None):
        if source is None:
            source = self._source_vertex
        shortest_paths = {}
        visited = set()
        for vertex in self.graph.keys():
            shortest_paths[vertex] = (np.inf, [])
        shortest_paths[source] = (0, [])
        visited.add(source)
        while set(self.graph.keys() - visited):
            source, min_edge = -1, ()
            for vertex in visited:
                for edge in self.graph[vertex]:
                    if edge[0] in visited:
                        continue
                    if not min_edge or shortest_paths[vertex][0] + edge[1] < min_edge[1]:
                        min_edge = (edge[0], shortest_paths[vertex][0] + edge[1])
                        source = vertex
            shortest_paths[min_edge[0]] = (min_edge[1], shortest_paths[source][1] + [min_edge[0]])
            visited.add(min_edge[0])
        return shortest_paths

if __name__ == '__main__':
    path_finder = DijkstraPathFinder('dijkstraData.txt')
    paths = path_finder.compute_shortest_paths()
    actual = {vertex: distance[0] for (vertex, distance) in paths.items()}
    query_point = [7,37,59,82,99,115,133,165,188,197]
    for i in query_point:
        print(actual[i])
