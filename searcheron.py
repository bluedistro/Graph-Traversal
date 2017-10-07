import sys
from PyQt4 import QtGui
from application import Search
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

__author__ = 'Biney Kingsley'

# TODO: PROGRAM THE RUNTIME


class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # instantiate the search class
        self.search = Search()

        # a figure instance to plot on
        self.figure = Figure()

        # instantiate horixontal and vertical layout boxes
        self.hbox = QtGui.QHBoxLayout()
        self.disp_hbox = QtGui.QHBoxLayout()
        self.layout = QtGui.QVBoxLayout()

        # TOP HORIZONTAL BOX
        # instantiate the labels
        self.algorithm_label = QtGui.QLabel()
        self.destination_label = QtGui.QLabel()

        # set text of the labels
        self.algorithm_label.setText('Algorithm')
        self.destination_label.setText('Destination')

        # instantiate the combo boxes
        self.algorithm_combo = QtGui.QComboBox()
        self.search_combo = QtGui.QComboBox()

        # pre-populate the combo boxes
        self.algorithm_combo.addItems(["Uninformed", "Informed"])
        self.search_combo.addItems(["Depth First", "Breadth First", "Uniform Cost"])

        # change the search_combobox values based on change in algorithm_combobox
        self.algos = {'Uninformed': ["Depth First", "Breadth First", "Uniform Cost"], 'Informed':['Greedy Best First', 'A* Search']}
        self.algorithm_combo.activated[str].connect(self.switch_algo)

        # Instantiate the button
        self.search_btn = QtGui.QPushButton('Go')
        self.search_btn.setToolTip('Search for Goal')

        # instantiate the textbox
        self.destination_input = QtGui.QLineEdit()

        # BOTTOM HORIZONTAL BOX

        # set font x'tics
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)

        # instantiate the labels
        self.disp_algorithm = QtGui.QLabel()
        self.disp_algorithm.setText('Algorithm:')
        self.disp_algorithm.setFont(font)
        self.disp_algorithm.setStyleSheet('color: blue')
        self.disp_start = QtGui.QLabel()
        self.disp_start.setText('Start:')
        self.disp_start.setFont(font)
        self.disp_start.setStyleSheet('color: blue')
        self.disp_end = QtGui.QLabel()
        self.disp_end.setText('End:')
        self.disp_end.setFont(font)
        self.disp_end.setStyleSheet('color: blue')
        self.disp_nodes_visited = QtGui.QLabel()
        self.disp_nodes_visited.setText('Nodes Visited:')
        self.disp_nodes_visited.setFont(font)
        self.disp_nodes_visited.setStyleSheet('color: blue')
        self.disp_runtime = QtGui.QLabel()
        self.disp_runtime.setText('Runtime:')
        self.disp_runtime.setFont(font)
        self.disp_runtime.setStyleSheet('color: blue')

        # add widgets to the top horizontal box layout
        self.hbox.addWidget(self.algorithm_combo)
        self.hbox.addStretch()
        self.hbox.addWidget(self.algorithm_label)
        self.hbox.addStretch()
        self.hbox.addWidget(self.search_combo)
        self.hbox.addStretch()
        self.hbox.addWidget(self.destination_label)
        self.hbox.addStretch()
        self.hbox.addWidget(self.destination_input)
        self.hbox.addStretch()
        self.hbox.addWidget(self.search_btn)
        self.hbox.addStretch()

        # add widgets to the bottom horizontal box layout
        self.disp_hbox.addWidget(self.disp_algorithm)
        self.hbox.addStretch()
        self.disp_hbox.addWidget(self.disp_start)
        self.hbox.addStretch()
        self.disp_hbox.addWidget(self.disp_end)
        self.hbox.addStretch()
        self.disp_hbox.addWidget(self.disp_nodes_visited)
        self.hbox.addStretch()
        self.disp_hbox.addWidget(self.disp_runtime)
        self.hbox.addStretch()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.search_btn.clicked.connect(self.plot)

        # set the layout => arrange the horizontal layouts and canvas in proper vertical order
        self.layout.addLayout(self.hbox)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.layout.addLayout(self.disp_hbox)
        self.setLayout(self.layout)

        # give a name to the program
        self.setWindowTitle('Searcheron')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    # used to switch the items in algorithm combobox based on the category of search selected
    def switch_algo(self, text):
        items = self.algos[str(text)]
        self.search_combo.clear()
        self.search_combo.addItems(items)

    # get the algorithm code name using its full name
    def get_algo(self, algorithm=None):
        algorithm_dict = {'Depth First':'dfs', 'Breadth First':'bfs', 'Uniform Cost':'ucs'}
        for i in range(len(algorithm_dict)):
            if algorithm == algorithm_dict.keys()[i]:
                algo = algorithm_dict.values()[i]
        return algo

    def plot(self):

        ubs_word = str(self.search_combo.currentText()) # name of the actual uninformed algorithm
        end = str(self.destination_input.text()) # name of goal

        # get the algorithm's code
        algo = self.get_algo(algorithm=ubs_word)

        # call the graphing function
        numpath, x_capa, y_capa, x_capitula, y_capitula, labella = self.search.gui_target(algorithm=algo, goal=end)
        # set the items to be displayed at the bottom of the page
        self.disp_algorithm.setText('Algorithm: {}'.format(ubs_word))
        self.disp_start.setText('Start: Accra')
        self.disp_end.setText('End: {}'.format(end))
        self.disp_nodes_visited.setText('Nodes Visited: {}'.format(str(numpath)))
        self.disp_runtime.setText('Runtime: 23ms')

        # make an initial full subplot
        plt = self.figure.add_subplot(111)

        # clear the canvas to make way for a new plot
        plt.clear()

        # plot a scatter diagram of all the states in the tree
        plt.scatter([x_capa[x] for x in range(len(x_capa))],
                    [y_capa[y] for y in range(len(y_capa))],
                    marker='o')

        for label, x, y in zip(labella, x_capa, y_capa):
            plt.annotate(label, xy=(x, y))

        # plot the actual path returned by the search algorithm
        plt.plot([x_capitula[x] for x in range(len(x_capitula))],
                 [y_capitula[y] for y in range(len(y_capitula))])

        # activate graph grid
        plt.grid()

        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
