from __future__ import print_function

'''
This class implements basic data structure classes which is used to implemented the various search  algorithms
'''


# Stacks class
class Stacks:

    def __init__(self):
        self.stackList = []

    def push(self, data):
        self.stackList.append(data)

    def pop(self):
        if self.isEmpty():
            print('')
            return

        data = self.stackList.pop()
        return data

    def top(self):
        if self.isEmpty():
            print('')
            return
        topindex = len(self.stackList)-1
        top = self.stackList[topindex]
        return top

    def isEmpty(self):
        if len(self.stackList) == 0:
            return True
        else:
            return False

    def getSize(self):
        return len(self.stackList)


# Queues class
class Queues:

    def __init__(self):
        self.QueuesList = []

    def clear(self):
        self.__init__()

    def enQueues(self, data):
        self.QueuesList.append(data)

    def deQueues(self):
        data = self.QueuesList.pop(0)
        return data

    def isEmpty(self):
        if len(self.QueuesList) == 0:
            return True
        else:
            return False

    def showStructure(self):
        for x in self.QueuesList:
            print(x, end='\t')


# Node Class
class Node:

    def __init__(self, key, x, y):
        # Arguments:
            # key: goal state
            # x: x coordinates
            # y: y coordinates
        self.child = []
        self.right = None
        self.left = None
        self.Queues = Queues()
        self.stack = Stacks()
        self.key = key
        self.cost = 0
        self.x = x
        self.y = y
        self.parent = None

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def setRight(self, Node):
        self.right = Node

    def setLeft(self, Node):
        self.left = Node

    def setKey(self, Node):
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

    def add_child(self, Node):
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

    def set_parent(self, Node):
        self.parent = Node

    def get_parent(self):
        return self.parent

