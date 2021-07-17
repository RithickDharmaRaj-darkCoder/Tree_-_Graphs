# Data Structure ...
# User-Defined ...
# Non-Linear ...
# Graphs ...
# Adjustancy Matrix Graph (Bi-Directional Graph) ...

class alrg:
    graph = {}

    def traversal(self):
        for i in self.graph:
            print(f'{i} = {self.graph.get(i)}')

    def add_node(self,v):
        if v in self.graph:
            print(f'{v} is already in graph!')
        else:
            self.graph[v] = []

    def add_edges(self,v1,v2):
        if v1 not in self.graph:
            print(f'{v1} is not in graph!')
        elif v2 not in self.graph:
            print(f'{v2} is not in graph!')
        else:
            if v2 not in self.graph[v1]:
                self.graph[v1].append(v2)
            if v1 not in self.graph[v2]:
                self.graph[v2].append(v1)

    '''def delete_node(self,v):
        if v not in self.graph:
            print(f'{v} is not in graph!')
        else:
            self.graph.pop(v)
            for i in self.graph:
                try:
                    self.graph[i].remove(v)
                except ValueError:
                    pass

    def delete_edge(self,v1,v2):
        if v1 not in self.graph:
            print(f'{v1} is not in graph!')
        elif v2 not in self.graph:
            print(f'{v2} is not in graph!')
        else:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)'''
