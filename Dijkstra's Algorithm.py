import sys
from heapq import heapify, heappush, heappop

class Graph:
    def __init__(self, Nodes):
        self.Nodes = Nodes
        self.adj_list = {}

        for i in self.Nodes:
            self.adj_list[i] = {}


    def add_edge(self, source, destination, edge_cost):
        self.adj_list[source][destination] = edge_cost
