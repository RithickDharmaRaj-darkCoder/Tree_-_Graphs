# Data Structure ...
# User-Defined ...
# Non-Linear ...
# Graphs ...
# Adjustancy Matrix Graph ...

def add_node(node):
    global node_count
    if node in nodes:
        print(f'{node} is already present in Graph!\n')
    else:
        node_count += 1
        nodes.append(node)
        temp = []
        for column in graph:
            column.append(0)
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
        #print(f'Nodes : {nodes}\nGraph : {graph}\n')

def traversal():
    for row in range(node_count):
        print(nodes[row],end=" ")
        for column in range(node_count):
            print(f'{graph[row] [column]}',end=" ")
        print()




nodes = []
node_count = 0
graph = []
traversal()