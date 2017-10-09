# NOTE: TO RUN IN CONSOLE MODE, UNCOMMENT THE self.reset() AND plt.show() INSTANCES IN THE gen_plot() METHOD
# AND OTHERWISE WHEN RUNNING IN GUI MODE

__author__ = 'Kingsley Biney'

# NB: To use this class, your tree class should implement the backtrack method

try:
    import matplotlib.pyplot as plt
except ImportError:
    msg = "Unable to import matplotlib.pyplot"
    raise ImportError(msg)


'''
 This class implements plotting techniques for visualizing implemented search algorithms
 It contains two main methods:
    * ubs_plotter -> implements visualization of search algorithms
    * gen_plot -> mother algorithm housing the engine of the plotting technique
 '''


class Plot_utils:

    def __init__(self, tree = None,  x_list = None, y_list = None, labels = None):

        # Arguments:
        # tree: the Binary tree graph
        # x_list: a list containing the x coordinates of all the nodes in the tree
        # y_list: a list containing the y coordinates of all the nodes in the tree
        # labels: a list containing the labels(names) of all the nodes in the tree

        self.tree = tree
        self.x_list = x_list
        self.y_list = y_list
        self.labels = labels
        self.path_list_x = []
        self.path_list_y = []
        self.path_key_list = []

    # clears the lists in it after each call (Used only when running in console)
    def reset(self):
        self.path_list_x = []
        self.path_list_y = []
        self.path_key_list = []

    # just a wrapper around the gen_plot method
    def ubs_plotter(self, path=None, algorithm=None):

        # Argument:
        # path: a list containing the labels of the nodes traversed in reaching the goal state
        # sorted in order
        # algorithm: search algorithm being used

        # Return
            # opt_len (int): the number of nodes visited by the ucs algorithm (used only by ucs algorithm)
            # x_capa (int list): all the x coordinates of the nodes in the tree
            # y_capa (int list): all the y coordinates of the nodes in the tree
            # x_capitula (int list): all the x coordinates of the nodes visited by algorithm in use
            # y_capitula (int list): all the y coordinates of the nodes visited by algorithm in use
            # labella (string list): all the names of the nodes visited by algorithm in use

        if algorithm == 'ucs':
            opt_len, x_capa, y_capa, x_capitula, y_capitula, labella = self.gen_plot(path=path, algorithm='ucs')
            return opt_len, x_capa, y_capa, x_capitula, y_capitula, labella
        if algorithm == 'bfs':
            x_capa, y_capa, x_capitula, y_capitula, labella  = self.gen_plot(path=path, algorithm='bfs')
            return x_capa, y_capa, x_capitula, y_capitula, labella
        if algorithm == 'dfs':
            x_capa, y_capa, x_capitula, y_capitula, labella = self.gen_plot(path=path, algorithm='dfs')
            return  x_capa, y_capa, x_capitula, y_capitula, labella

    def gen_plot(self, path=None, algorithm=None):

        # Arguments:
            # path: a list containing the labels of the nodes traversed in reaching the goal state
            # sorted in order
            # algorithm (string -> search algo code): for controlling the algorithm for plotting the
            #  various searching algorithms

        # Return:
            # opt_len (int): the number of nodes visited by the ucs algorithm (used only by ucs algorithm)
            # self.x_list (int list): all the x coordinates of the nodes in the tree
            # self.y_list (int list): all the y coordinates of the nodes in the tree
            # self.path_list_x (int list): all the x coordinates of the nodes visited by algorithm in use
            # self.path_list_y (int list): all the y coordinates of the nodes visited by algorithm in use
            # self.labels (string list): all the names of the nodes visited by algorithm in use

        # Breadth First Search and Depth First search use the same plotting technique
        if algorithm == 'bfs' or algorithm == 'dfs':

            # plot a scatter diagram of all the nodes in the graph
            plt.scatter([self.x_list[x] for x in range(len(self.x_list))],
                        [self.y_list[y] for y in range(len(self.y_list))],
                        marker='o', cmap=plt.get_cmap('Spectral'))

            # indicate respective labels on each node
            for label, x, y in zip(self.labels, self.x_list, self.y_list):
                plt.annotate(label, xy=(x, y))

            # grid the graph
            plt.grid()

            # compare labels in the algorithm's return graph list and main graph list and obtain corresponding
            #  xy coordinates from the main graph's x and y lists
            for j in range(len(path)):
                for i in range(len(self.labels)):
                    if self.labels[i] == path[j]:
                        self.path_list_x.append(self.x_list[i])
                        self.path_list_y.append(self.y_list[i])
                        self.path_key_list.append(self.labels[i])

            # plot the obtained xy lists obtained from the main graph
            plt.plot([self.path_list_x[x] for x in range(len(self.path_list_x))],
                     [self.path_list_y[y] for y in range(len(self.path_list_y))])

            '''uncomment when running in console mode and comment when running in gui mode'''
            # plt.show()
            # self.reset()
            return  self.x_list, self.y_list, self.path_list_x, self.path_list_y, self.labels

        # Uniform Cost search uses a different plotting technique due to presence of backtrack
        elif algorithm == 'ucs':
            opt_path_list = []
            optimized_path = self.tree.backtrack(path[0], path[-1])

            # get the actual values of the nodes in the optimized path and append to opt_path_list
            for i in range(len(optimized_path)):
                opt_path_list.append(optimized_path[i].getKey())

            # plot a scatter diagram of all the nodes in the graph
            plt.scatter([self.x_list[x] for x in range(len(self.x_list))],
                        [self.y_list[y] for y in range(len(self.y_list))],
                        marker='s', cmap=plt.get_cmap('Spectral'))

            # indicate respective labels on each node
            for label, x, y in zip(self.labels, self.x_list, self.y_list):
                plt.annotate(label, xy=(x, y))

            # grid the graph
            plt.grid()
            # compare labels in the optimized path list and main graph list and obtain corresponding
            #  xy coordinates from the main graph's x and y lists
            for j in range(len(opt_path_list)):
                for i in range(len(self.labels)):
                    if self.labels[i] == opt_path_list[j]:
                        self.path_list_x.append(self.x_list[i])
                        self.path_list_y.append(self.y_list[i])
                        self.path_key_list.append(self.labels[i])

            # plot the obtained xy lists obtained from the main graph
            plt.plot([self.path_list_x[x] for x in range(len(self.path_list_x))],
                     [self.path_list_y[y] for y in range(len(self.path_list_y))])

            # save the number of nodes traversed from the initial state to the goal state
            opt_len = len(opt_path_list)

            '''uncomment when running in console mode and comment when running in gui mode'''
            # plt.show()
            # self.reset()

            return opt_len, self.x_list, self.y_list, self.path_list_x, self.path_list_y, self.labels
