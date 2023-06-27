# Directed Graph

class Graph:
    def __init__(self, Nodes):
        self.Nodes = Nodes
        self.adj_list = {}

        for i in self.Nodes:
            self.adj_list[i] = []

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)

    #BFS implementation
    def BFS(self, start_node):
        queue = []
        found = {}
        for i in self.adj_list.keys():
            found[i] = False

        queue.append(start_node)
        found[start_node] = True

        while queue:
            item = queue.pop(0)
            print(' -> ', item, end='')

            for i in self.adj_list[item]:
                 if not found[i]:
                     queue.append(i)
                     found[i] = True

    #DFS Implementation
    def DFS(self, start_node):
        print()
        stack = []
        found = {}
        for i in self.adj_list.keys():
            found[i] = False

        stack.append(start_node)

        while stack:
            item = stack.pop()
            if not found[item]:
                print(' -> ', item, end='')
                found[item] = True

            for i in self.adj_list[item]:
                stack.append(i)


graph1 = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

graph1.add_edge('A', 'B')
graph1.add_edge('D', 'C')
graph1.add_edge('D', 'E')
graph1.add_edge('D', 'F')
graph1.add_edge('E', 'G')
graph1.add_edge('F', 'C')
graph1.add_edge('G', 'D')
graph1.add_edge('G', 'H')
graph1.add_edge('H', 'A')
graph1.add_edge('H', 'B')

graph1.BFS('D')
graph1.DFS('D')
