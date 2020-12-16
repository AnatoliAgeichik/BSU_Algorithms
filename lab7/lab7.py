import random
import time
import plotly.express as px
import pandas

class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=data

class Tree:
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root

    def add(self, data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._add(data, self.root)




    def _add(self,data, node:Node):
        if data<node.data:
            if node.left is None:
                node.left=Node(data)
            else:
                self._add(data, node.left)
        else:
            if node.right is None:
                node.right=Node(data)
            else:
                self._add(data, node.right)

    def find(self, data):
        if self.root is None:
            return None
        else:
            self._find(data, self.root)

    def _find(self, data, node:Node):
        if data == node.data:
            print(node.data)
            #return node.data
        elif data< node.data and node.left is not None:
            self._find(data, node.left)
        elif data > node.data and node.right is not None:
            self._find(data, node.right)
        else:
             return None

    def print(self):
        if self.root is not None:
            self._print(self.root,0)

    def _print(self, node, level):
        if node != None:
            self._print(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self._print(node.right, level + 1)


tree = Tree()
# tree.add(3)
# tree.add(1)
# tree.add(4)
# tree.add(0)
# #
# tree.add(8)
# tree.add(2)
for i in range(20):
    tree.add(random.randint(0,160))
n=20
count=25000
chart_data=[]
for i in range(5):
    for _ in range(20):
        tree.add(random.randint(0, 160))

    n+=20
    start_time = time.time()
    for j in range(count):
        tree.find(random.randint(0,160))
    res_time = time.time() - start_time
    chart_data.append(dict(size=n, time=res_time))
    #count+=15000
#tree.add(3)
fig = px.line(chart_data, x="size", y="time")
fig.show()
tree.print()
x=tree.find(0)
print(type(x))
print(tree.find(0))
#print(tree.find(10))


