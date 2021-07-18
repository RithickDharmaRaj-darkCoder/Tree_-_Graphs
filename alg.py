# Data Structure ...
# User-Defined ...
# Non-Linear ...
# Graphs ...
# Adjustancy List Representing Graph (Bi-Directional-Weighted Graph) ...

class alrg:
    graph = {}
    visited = []

    def traversal(self,starting_node):
        print('List Representation ...')
        for i in self.graph:
            print(f'    {i} = {self.graph.get(i)}')
        print('Depth First Search Representation ...\n\tDFS :',end=" ")
        self.dfs(starting_node)

    def dfs(self,starting_node):
        if starting_node not in self.graph:
            print(f'{starting_node} is not in Graph!')
        else:
            if starting_node not in self.visited:
                print(starting_node,end=" ")
                self.visited.append(starting_node)
                for inn in range(len(self.graph[starting_node])):
                    self.dfs(self.graph[starting_node][inn][0])

    def add_node(self,v):
        if v in self.graph:
            print(f'{v} is already in graph!')
        else:
            self.graph[v] = []

    def add_edges(self,v1,v2,w):
        if v1 not in self.graph:
            print(f'{v1} is not in graph!')
        elif v2 not in self.graph:
            print(f'{v2} is not in graph!')
        else:
            lst1 = [v2,w]
            lst2 = [v1,w]
            if v2 not in self.graph[v1]:
                self.graph[v1].append(lst1)
            if v1 not in self.graph[v2]:
                self.graph[v2].append(lst2)

    def delete_node(self,v):
        if v not in self.graph:
            print(f'{v} is not in graph!')
        else:
            self.graph.pop(v)
            for keys in self.graph:
                for outer in range(len(self.graph[keys])):
                    if self.graph[keys][outer][0] == v:
                        self.graph[keys].pop(outer)

    def delete_edge(self,v1,v2):
        if v1 not in self.graph:
            print(f'{v1} is not in graph!')
        elif v2 not in self.graph:
            print(f'{v2} is not in graph!')
        else:
            #self.graph[v1].remove(v2)
            #self.graph[v2].remove(v1)
            for outer in range(len(self.graph[v1])):
                if self.graph[v1][outer][0] == v2:
                    del self.graph[v1][outer]
            for out in range(len(self.graph[v2])):
                try:
                    if self.graph[v2][out][0] == v1:
                        del self.graph[v2][out]
                except IndexError:
                    pass
