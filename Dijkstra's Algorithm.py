import sys
from heapq import heapify, heappush, heappop

class Graph:
    def __init__(self, Nodes):
        self.Nodes = Nodes
        self.adj_list = {}
        self.visited = []
        self.predecessor = {}
        self.path = []
        self.node_cost = {}

        for i in self.Nodes:
            self.adj_list[i] = {}


    def add_edge(self, source, destination, edge_cost):
        self.adj_list[source][destination] = edge_cost


    def dijkstra(self, start, goal):
        infinity = sys.maxsize
        self.temp_graph = self.adj_list

        for i in self.temp_graph:
            self.node_cost[i] = infinity
        self.node_cost[start] = 0

        min_node = start
        for i in range(len(self.temp_graph.keys())-1):
            if min_node not in self.visited:
                self.visited.append(min_node)
                min_heap = []
                for j in self.temp_graph[min_node]:
                    if self.node_cost[min_node] + self.temp_graph[min_node][j] < self.node_cost[j]:
                        self.node_cost[j] = self.node_cost[min_node] + self.temp_graph[min_node][j]
                        self.predecessor[j] = min_node
                    heappush(min_heap, (self.node_cost[j], j))

            heapify(min_heap)
            min_node = min_heap[0][1]

        current_node = goal

        while current_node != start:
            try:
                self.path.insert(0, current_node)
                current_node = self.predecessor[current_node]

            except Exception as e:
                print(e)
                break

        self.path.insert(0, start)


        if self.node_cost[goal] != infinity:
            print('Shortest distance : ', self.node_cost[goal])
            print('Shortest path is : ', self.path)




graph = Graph(['a','b','c','d','e','f','g','h',])

graph.add_edge('a', 'b', 3)
graph.add_edge('a', 'c', 4)
graph.add_edge('a', 'd', 7)
graph.add_edge('b', 'c', 1)
graph.add_edge('b', 'f', 5)
graph.add_edge('c', 'f', 6)
graph.add_edge('c', 'd', 2)
graph.add_edge('d', 'e', 3)
graph.add_edge('d', 'g', 6)
graph.add_edge('e', 'g', 3)
graph.add_edge('e', 'h', 4)
graph.add_edge('f', 'e', 1)
graph.add_edge('f', 'h', 8)
graph.add_edge('g', 'h', 2)
graph.add_edge('h', 'g', 2)

graph.dijkstra('a', 'h')







