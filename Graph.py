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
    def BFS(self, start_node, destination_node):
        print()
        queue = []
        found = {}
        for i in self.adj_list.keys():
            found[i] = False

        queue.append(start_node)
        found[start_node] = True

        while queue:
            item = queue.pop(0)
            print(' -> ', item, end='')

            if item == destination_node:
                break

            for i in self.adj_list[item]:
                 if not found[i]:
                     queue.append(i)
                     found[i] = True

    #DFS Implementation
    def DFS(self, start_node, destination_node):
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

                if item == destination_node:
                    break

                for i in self.adj_list[item]:
                    if not found[i]:
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

graph1.BFS('D', 'B')
graph1.DFS('D', 'A')

graph1.BFS('D','H')
graph1.DFS('D','H')
