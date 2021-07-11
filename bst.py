# Data Structure ...
# User-Defined ...
# Non-Linear ...
# Trees ...
# Binary Search Tree ...

class bst:
    def __init__(self,Object_name,key=None):
        self.Object_name = Object_name
        self.key = key
        self.lchild = None
        self.rchild = None

    def pre_order_traversal(self):
        print(f'{self.Object_name}[Pre-order] : ',end=" ")
        if not self.key:
            print('Binary Search tree is Empty!')
        elif self.key:
            print(f'{self.key}, ',end=" ")
            if self.lchild:
                self.lchild.pre_order_traversal()
            elif self.rchild:
                self.rchild.pre_order_traversal()


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


bst1 = bst('BST1',10)

bst1.pre_order_traversal()