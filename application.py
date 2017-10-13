from __future__ import print_function

__author__ = 'Kingsley Biney'

try:
    from BinaryTree import BinaryTree
    from plot_utils import Plot_utils as plutils
    from maps import Maps
    from datetime import datetime
    from data_structs import Node
except ImportError:
    msg = "Unable to import some packages"
    raise ImportError(msg)

'''
This class provides a high level implementation of the methods in plot_utils class
It contains three main methods:
    * create_extended_map -> to create the complete graph to be traversed
    * gui_taget -> provides call for gui visualization and interaction
    * console_target -> provides call console visualization and interaction
    
Other available methods are the disp_in_order, disp_pre_order and disp_post_order
'''


class Search:

    def __init__(self):
        self.x_list = []
        self.y_list = []
        self.labels = []
        self.tree = BinaryTree()
        self.maps = Maps(x_list=self.x_list, y_list=self.y_list, labels=self.labels, tree=self.tree)
        self.graph = None
        self.number_path = None

    def dis_in_order(self):
        self.x_list, self.y_list, self.labels, self.tree = self.maps.original_map()
        print(self.tree.displayInOrder(self.tree.root))

    def dis_pre_order(self):
        self.x_list, self.y_list, self.labels, self.tree = self.maps.original_map()
        self.tree.displayPreOrder(self.tree.root)

    def dis_post_order(self):
        self.x_list, self.y_list, self.labels, self.tree = self.maps.original_map()
        self.tree.displayPostOrder(self.tree.root)

    # wrapper around the A* and Greedy Depth First Search method
    def isa(self, searchKey=None, algorithm=None):
        for i in range(len(self.labels)):
            if searchKey == self.labels[i]:
                x_coord_holder = self.x_list[i]
                y_coord_holder = self.y_list[i]
        # print('isa x: '  + str(x_coord_holder))
        if algorithm == 'gbfs':
            path = self.tree.gbfs(searchKey=searchKey, x=x_coord_holder, y=y_coord_holder)
        elif algorithm == 'asts':
            path = self.tree.asts(searchKey=searchKey, x=x_coord_holder, y=y_coord_holder)
        return path



    # Implement Uninformed Blind Search Algorithms on GUI
    def gui_target(self, map=None, algorithm=None, goal=None):

        # Arguments:
            # algorithm (string): the search algorithm code to be used
            # goal (string): the city (Node) being searched for (goal state)

        # Returns:
            # numpath (int): the number of Nodes visited by the algorithm in use
            # x_capa (int list): all the x coordinates of the Nodes in the tree
            # y_capa (int list): all the y coordinates of the Nodes in the tree
            # x_capitula (int list): all the x coordinates of the Nodes visited by algorithm in use
            # y_capitula (int list): all the y coordinates of the Nodes visited by algorithm in use
            # labella (string list): all the names of the Nodes visited by algorithm in use

        # clear the canvas
        self.maps.reset()

        # create the binary tree to be used
        if map == 'original':
            self.x_list, self.y_list, self.labels, self.tree = self.maps.original_map()
        elif map == 'extended':
            self.x_list, self.y_list, self.labels, self.tree = self.maps.extended_map()

        # instantiate the plot_utils class
        pltls = plutils(tree=self.tree, x_list=self.x_list, y_list=self.y_list, labels=self.labels)

        if algorithm == 'ucs':
            start = datetime.now().microsecond
            path = self.tree.ucs(goal)
            stop = datetime.now().microsecond
            time_taken = stop - start
            print('Nodes Traversed in uniform cost: ', end='\t')
            for i in range(len(path)):
                print(path[i].getKey(), end='\t')
            print('\n')
            numpath, x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='ucs')

        elif algorithm == 'dfs':
            start = datetime.now().microsecond
            path = self.tree.dfs(goal)
            stop = datetime.now().microsecond
            time_taken = stop - start
            print('Nodes Traversed in depth first: ')
            for i in range(len(path)):
                print(path[i].getKey(), end='\t')
            print('\n')
            numpath, x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='dfs')

        elif algorithm == 'bfs':
            start = datetime.now().microsecond
            path = self.tree.bfs(goal)
            stop = datetime.now().microsecond
            time_taken = stop - start
            print('Nodes Traversed in breadth first: ')
            for i in range(len(path)):
                print(path[i].getKey(), end='\t')
            print('\n')
            numpath, x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='bfs')

        elif algorithm == 'gbfs':
            start = datetime.now().microsecond
            path = self.isa(searchKey=goal, algorithm=algorithm)
            stop = datetime.now().microsecond
            time_taken = stop - start
            print('Nodes Traversed in greedy best first: ')
            for i in range(len(path)):
                print(path[i].getKey(), end='\t')
            print('\n')
            numpath, x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='gbfs')

        elif algorithm == 'asts':
            start = datetime.now().microsecond
            path = self.isa(searchKey=goal, algorithm=algorithm)
            stop = datetime.now().microsecond
            time_taken = stop - start
            print('Nodes Traversed in a star best first: ')
            for i in range(len(path)):
                print(path[i].getKey(), end='\t')
            print('\n')
            numpath, x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='asts')

        # return the necessary variables
        return time_taken, numpath, x_capa, y_capa, x_capitula, y_capitula, labella

    # Implement Uninformed Blind Search Algorithms on console
    def console_target(self):
        print('Implemented algorithm codes: ucs, dfs, bfs, gbfs, asts')
        map = raw_input('Map Selection: enter "original" or "extended": ').lower()

        # clear the canvas
        self.maps.reset()

        # create the binary tree to be used
        if map == 'original':
            self.x_list, self.y_list, self.labels, self.tree = self.maps.original_map()
        elif map == 'extended':
            self.x_list, self.y_list, self.labels, self.tree = self.maps.extended_map()

        # instantiate the plutils class
        pltls = plutils(tree=self.tree, x_list=self.x_list, y_list=self.y_list, labels=self.labels)

        while True:
            goal = raw_input('Enter the name of the city: ')
            algorithm = raw_input('Enter search algorithm code: ').lower()

            if algorithm == 'ucs':
                path = self.tree.ucs(goal)
                num_path, _, _, _, _, _ = pltls.ubs_plotter(path=path, algorithm=algorithm)
                print('number of Nodes visited: {}'.format(num_path))

            elif algorithm == 'bfs':
                path = self.tree.bfs(goal)
                num_path = len(path)
                print('number of Nodes visited: {}'.format(num_path))
                pltls.ubs_plotter(path=path, algorithm=algorithm)

            elif algorithm == 'dfs':
                path = self.tree.dfs(goal)
                num_path = len(path)
                print('number of Nodes visited: {}'.format(num_path))
                pltls.ubs_plotter(path=path, algorithm=algorithm)

            elif algorithm == 'gbfs':
                path = self.isa(searchKey=goal, algorithm=algorithm)
                num_path = len(path)
                print(path)
                print('number of Nodes visited: {}'.format(num_path))
                pltls.ubs_plotter(path=path, algorithm=algorithm)

            elif algorithm == 'asts':
                path = self.isa(searchKey=goal, algorithm=algorithm)
                num_path = len(path)
                print(path)
                print('number of Nodes visited: {}'.format(num_path))
                pltls.ubs_plotter(path=path, algorithm=algorithm)

            # elif algorithm == 'disno':
            #     self.dis_in_order()
            #
            # elif algorithm == 'dpreo':
            #     self.dis_pre_order()
            #
            # elif algorithm == 'dposo':
            #     self.dis_post_order()

            else:
                raise 'Invalid argument entered'

