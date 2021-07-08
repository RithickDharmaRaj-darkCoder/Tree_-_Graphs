# Data Structure ...
# User-Defined ...
# Non-Linear ...
# Trees ...
# Binary Search Tree ...

class bst:
    def __init__(self, key=None):
        self.key = key
        self.lchild = None
        self.rchild = None

    def add_node(self, data):
        if not self.key:
            self.key = data
            return
        if data < self.key:
            if self.lchild:
                self.lchild.add_node(data)
            else:
                self.lchild = bst(data)
        elif data == self.key:
            return
        else:
            if self.rchild:
                self.rchild.add_node(data)
            else:
                self.rchild = bst(data)