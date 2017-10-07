from __future__ import print_function

__author__ = 'Kingsley Biney'
try:
    from BinaryTree import BinaryTree
    from plot_utils import Plot_utils as plutils
    from data_structs import Node
except ImportError:
    msg = "Unable to import some packages"
    raise ImportError(msg)

'''
This class provides a high level implementation of the methods in plot_utils class
It contains three main methods:
    * create_tree -> to create the complete graph to be traversed
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
        self.graph = None
        self.number_path = None

    def create_tree(self):
        x = Node("Accra", 0, 200)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert(None, x, 'LEFT')

        x = Node("Tema", 40, 120)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Accra", x, 'LEFT')

        x = Node("Achimota", 80, 180)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Accra", x, 'RIGHT')

        x = Node('Dansoman', 80, 120)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Achimota", x, 'LEFT')

        x = Node('Kaneshie', 60, 80)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Dansoman", x, 'LEFT')

        x = Node('Mamprobi', 100, 80)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Dansoman", x, 'RIGHT')

        x = Node('Kasoa', 100, 160)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Achimota", x, 'RIGHT')

        x = Node('Boduase', 140, 140)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Kasoa", x, 'LEFT')

        x = Node('Mankessim', 140, 180)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Kasoa", x, 'RIGHT')

    def dis_in_order(self):
        self.create_tree()
        print(self.tree.displayInOrder(self.tree.root))

    def dis_pre_order(self):
        self.create_tree()
        self.tree.displayPreOrder(self.tree.root)

    def dis_post_order(self):
        self.create_tree()
        self.tree.displayPostOrder(self.tree.root)

    # Implement Uninformed Blind Search Algorithms on GUI
    def gui_target(self, algorithm=None, goal=None):

        # Arguments:
            # algorithm (string): the search algorithm code to be used
            # goal (string): the city (node) being searched for (goal state)

        # Returns:
            # numpath (int): the number of nodes visited by the algorithm in use
            # x_capa (int list): all the x coordinates of the nodes in the tree
            # y_capa (int list): all the y coordinates of the nodes in the tree
            # x_capitula (int list): all the x coordinates of the nodes visited by algorithm in use
            # y_capitula (int list): all the y coordinates of the nodes visited by algorithm in use
            # labella (string list): all the names of the nodes visited by algorithm in use

        # create the binary tree to be used
        self.create_tree()

        # instantiate the plot_utils class
        pltls = plutils(tree=self.tree, x_list=self.x_list, y_list=self.y_list, labels=self.labels)

        if algorithm == 'ucs':
            path = self.tree.ucs(goal)
            numpath, x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='ucs')

        elif algorithm == 'dfs':
            path = self.tree.dfs(goal)
            numpath = len(path)
            x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='dfs')

        elif algorithm == 'bfs':
            path = self.tree.bfs(goal)
            numpath = len(path)
            x_capa, y_capa, x_capitula, y_capitula, labella = pltls.ubs_plotter(path=path, algorithm='bfs')

        # return the necessary variables
        return numpath, x_capa, y_capa, x_capitula, y_capitula, labella

    # Implement Uninformed Blind Search Algorithms on console
    def console_target(self):
        print('Implemented algorithm codes: ucs, dfs, bfs')
        self.create_tree()

        # instantiate the plutils class
        pltls = plutils(tree=self.tree, x_list=self.x_list, y_list=self.y_list, labels=self.labels)

        while True:
            goal = raw_input('Enter the name of the city: ')
            algorithm = raw_input('Enter search algorithm code: ')
            algorithm = algorithm.lower()

            if algorithm == 'ucs':
                path = self.tree.ucs(goal)
                num_path, _, _, _, _, _ = pltls.ubs_plotter(path=path, algorithm=algorithm)
                print('number of nodes visited: {}'.format(num_path))

            elif algorithm == 'bfs':
                path = self.tree.bfs(goal)
                num_path = len(path)
                print('number of nodes visited: {}'.format(num_path))
                pltls.ubs_plotter(path=path, algorithm=algorithm)

            elif algorithm == 'dfs':
                path = self.tree.dfs(goal)
                num_path = len(path)
                print('number of nodes visited: {}'.format(num_path))
                pltls.ubs_plotter(path=path, algorithm=algorithm)

            # TODO: FIX LITTLE TECHNICAL GLITCHES IN THESE ALGORITHM
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

