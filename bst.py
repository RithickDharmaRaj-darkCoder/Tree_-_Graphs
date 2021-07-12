# Data Structure ...
# User-Defined ...
# Non-Linear ...
# Trees ...
# Binary Search Tree ...

class bst:
    def __init__(self,key=None):
        self.key = key
        self.lchild = None
        self.rchild = None

    def traversal(self):
        print(f'Pre-Order  : ', end=" ")
        self.pre_order_traversal()
        print(f'\nIn-Order   : ',end=" ")
        self.in_order_traversal()
        print(f'\nPost-Order : ', end=" ")
        self.post_order_traversal()
        print('\n')

    def pre_order_traversal(self):
        if not self.key:
            print('Binary Search tree is Empty!')
        elif self.key:
            print(f'{self.key}',end=",")
            if self.lchild:
                self.lchild.pre_order_traversal()
            if self.rchild:
                self.rchild.pre_order_traversal()

    def in_order_traversal(self):
        if not self.key:
            print('Binary Search tree is Empty!')
        else:
            if self.lchild:
                self.lchild.in_order_traversal()
            print(f'{self.key}',end=',')
            if self.rchild:
                self.rchild.in_order_traversal()

    def post_order_traversal(self):
        if not self.key:
            print('Binary Search tree is Empty!')
        else:
            if self.lchild:
                self.lchild.post_order_traversal()
            if self.rchild:
                self.rchild.post_order_traversal()
            print(f'{self.key}',end=',')

    def find(self,x):
        print()
        if not self.key:
            print('Binary Search tree is Empty!')
            return
        if x == self.key:
            print(f'{x} is found in BST!')
        elif x < self.key:
            if not self.lchild:
                print(f'{x} is not in BST!')
            else:
                self.lchild.find(x)
        elif x > self.key:
            if not self.rchild:
                print(f'{x} is not in BST!')
            else:
                self.rchild.find(x)

    def insert(self, data):
        if not self.key:
            self.key = data
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = bst(key=data)
        elif data == self.key:
            return
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = bst(key=data)

