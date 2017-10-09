from __future__ import print_function

__author__ = 'Biney Kingsley'

'''
This class implements basic data structure classes which is used to implemented the various search  algorithms
'''


# Stacks class
class Stacks:

    def __init__(self):
        self.stackList = []

    def clear(self):
        self.__init__()

    def push(self, data):
        self.stackList.append(data)

    def pop(self):
        if self.isEmpty():
            return
        return self.stackList.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.stackList[-1]

    def isEmpty(self):
        if self.size() == 0:
            return True

    def size(self):
        return len(self.stackList)


# Queues class
class Queues:

    def __init__(self):
        self.queueList = []

    def clear(self):
        self.__init__()

    def enqueue(self, data):
        self.queueList.append(data)

    def get_last_element(self):
        return self.queueList[-1]

    def dequeue(self):
        item = self.queueList[0]
        self.queueList.remove(item)
        return item

    def isEmpty(self):
        if self.size() == 0:
            return True

    def showStructure(self):
        for x in self.queueList:
            print(x, end='\t')

    def size(self):
        return len(self.queueList)


# Node Class
class Node:

    def __init__(self, key=None, x_coord=None, y_coord=None):
        # Arguments:
            # key: goal state
            # x_coord: x coordinates
            # y_coord: y coordinates
        self.child = []
        self.right = None
        self.left = None
        self.Queues = Queues()
        self.stack = Stacks()
        self.key = key
        self.cost = 0
        self.x = x_coord
        self.y = y_coord
        self.parent = None

    def set_x(self, x_coord=None):
        self.x = x_coord

    def get_x(self):
        return self.x

    def set_y(self, y_coord=None):
        self.y = y_coord

    def get_y(self):
        return self.y

    def set_cost(self, cost=None):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def setRight(self, Node=None):
        self.right = Node

    def setLeft(self, Node=None):
        self.left = Node

    def setKey(self, Node=None):
        self.key = Node

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getKey(self):
        return self.key

    def hasLeft(self):
        status = False
        if self.left is not None:
            status = True
        else:
            status = False
        return status

    def hasRight(self):
        status = False
        if self.right is not None:
            status = True
        else:
            status = False
        return status

    def add_child(self, Node=None):
        self.child.append(Node)

    def first_child(self):
        return self.child.pop(0)

    def has_child(self):
        state = False
        if len(self.child) == 0:
            state = False
        else:
            state = True
        return state

    def set_parent(self, Node=None):
        self.parent = Node

    def get_parent(self):
        return self.parent

