# Data Structure ...
# User-Defined ...
# Non-Linear ...
# Graphs ...
# Adjustancy Matrix Graph (Bi-Directional Graph) ...

class amg:
    nodes = []
    node_count = 0
    graphs =[]

    def traversal(self):
        print('    ',end="")
        for i in self.nodes:
            print(format(i,"<3"),end="  ")
        print()
        for row in range(self.node_count):
            print(self.nodes[row],end="   ")
            for column in range(self.node_count):
                print(f'{format(self.graphs[row][column],"<3")}',end="  ")
            print()

    def add_node(self,variable):
        if variable in self.nodes:
            print(f'{variable} is already present!')
        else:
            self.node_count += 1
            self.nodes.append(variable)
            for column in self.graphs:
                column.append(0)
            temp = []
            for i in range(self.node_count):
                temp.append(0)
            self.graphs.append(temp)

    def add_edge(self,v1,v2):
        if v1 not in self.nodes:
            print(f'{v1} is not in graph\n')
        elif v2 not in self.nodes:
            print(f'{v2} is not in graph')
        else:
            self.graphs[self.nodes.index(v1)][self.nodes.index(v2)] = 1
            self.graphs[self.nodes.index(v2)][self.nodes.index(v1)] = 1