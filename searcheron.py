import sys, time
import numpy as np
from PyQt4 import QtGui, QtCore
from application import Search
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

__author__ = 'Biney Kingsley'

# TODO: PROGRAM THE RUNTIME


class Searcheron(QtGui.QDialog):

    # design UI
    def __init__(self, parent=None):
        super(Searcheron, self).__init__(parent)

        # instantiate the search class
        self.search = Search()

        # a figure instance to plot on
        self.figure = Figure()

        # display error messagebox
        self.errmsgbx = QtGui.QMessageBox()
        self.errmsgbx.setIcon(QtGui.QMessageBox.Warning)
        self.errmsgbx.setWindowTitle("Invalid Destination")

        # instantiate horixontal and vertical layout boxes
        self.hbox = QtGui.QHBoxLayout()
        self.disp_hbox = QtGui.QHBoxLayout()
        self.layout = QtGui.QVBoxLayout()

        # TOP HORIZONTAL BOX
        # instantiate the labels
        self.select_maps_label = QtGui.QLabel()
        self.select_search_category_label = QtGui.QLabel()
        self.algorithm_label = QtGui.QLabel()
        self.destination_label = QtGui.QLabel()

        # set text of the labels
        self.select_maps_label.setText('Map:')
        self.select_search_category_label.setText('Category:')
        self.algorithm_label.setText('Algorithm:')
        self.destination_label.setText('Destination:')

        # instantiate the combo boxes
        self.algorithm_combo = QtGui.QComboBox()
        self.search_combo = QtGui.QComboBox()
        self.select_map_combo = QtGui.QComboBox()

        # pre-populate the combo boxes
        self.algorithm_combo.addItems(["Uninformed", "Informed"])
        self.search_combo.addItems(["Depth First", "Breadth First", "Uniform Cost"])
        self.select_map_combo.addItems(["Original", "Extended"])

        # change the search_combobox values based on change in algorithm_combobox
        self.algos = {'Uninformed': ["Depth First", "Breadth First", "Uniform Cost"], 'Informed':['Greedy Best First', 'A* Search']}
        self.algorithm_combo.activated[str].connect(self.switch_algo)

        # Instantiate the button
        self.search_btn = QtGui.QPushButton('Go')

        # instantiate the textbox
        self.destination_input = QtGui.QLineEdit()
        self.destination_input.setPlaceholderText('enter available dest.')

        # set tooltips
        self.algorithm_combo.setToolTip('Select category of search algorithm')
        self.search_combo.setToolTip('Select search algorithm')
        self.search_btn.setToolTip('Search for Goal')

        # set locations for original map
        self.orig_dest = ['Accra', 'Tema', 'Achimota', 'Kasoa', ' Mamprobi', 'Dansoman','Kaneshie',
                          'Boduase', 'Mankessim']

        # set locations for extended map
        self.ext_dest = ['Accra', 'Tema', 'Achimota', 'Kasoa',' Mamprobi', 'Dansoman', 'Kaneshie',
                         'Boduase', 'Mankessim', 'Korle Gono', 'James Town', 'Russia', 'Bubuashie',
                         'Tesano', 'Kakum', 'Elmina', 'Cape Coast', 'Takoradi']

        # set tooltip to aid destination determination in destination_input field

        # just to preset tooltips before map combo box is engaged, not that really important
        self.destination_input.setToolTip('MAP LOCATIONS \n\b {}'.format("\n".join(self.orig_dest)))

        # do map tooltip settings
        self.map_tooltip = {'Original':self.orig_dest, 'Extended': self.ext_dest}
        self.select_map_combo.activated[str].connect(self.switch_maps_tooltip)

        # BOTTOM HORIZONTAL BOX

        # set font aesthetic x'tics
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setOverline(True)
        font.setUnderline(True)
        font.setFamily('Times')

        # instantiate the labels keys
        self.disp_algorithm = QtGui.QLabel()
        self.disp_algorithm.setText('Algorithm: None')
        self.disp_algorithm.setFont(font)
        self.disp_algorithm.setStyleSheet('color: blue')
        self.disp_start = QtGui.QLabel()
        self.disp_start.setText('Start: None')
        self.disp_start.setFont(font)
        self.disp_start.setStyleSheet('color: blue')
        self.disp_end = QtGui.QLabel()
        self.disp_end.setText('End: None')
        self.disp_end.setFont(font)
        self.disp_end.setStyleSheet('color: blue')
        self.disp_nodes_visited = QtGui.QLabel()
        self.disp_nodes_visited.setText('Nodes Visited: None')
        self.disp_nodes_visited.setFont(font)
        self.disp_nodes_visited.setStyleSheet('color: blue')
        self.disp_runtime = QtGui.QLabel()
        self.disp_runtime.setText('Runtime: None')
        self.disp_runtime.setFont(font)
        self.disp_runtime.setStyleSheet('color: blue')


        # add widgets to the top horizontal box layout
        self.hbox.addWidget(self.select_maps_label)
        self.hbox.addStretch()
        self.hbox.addWidget(self.select_map_combo)
        self.hbox.addStretch()
        self.hbox.addWidget(self.select_search_category_label)
        self.hbox.addStretch()
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

        # display default graph on first run
        self.default_plot()

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

        # set program name and icon
        self.setWindowTitle('Searcheron-v1.0.1 (Powered by Matplotlib-v1.5.1)')
        self.setWindowIcon(QtGui.QIcon('icon.png'))




        '''GUI Support Methods'''
    # switch the items in algorithm combobox based on the category of search selected
    def switch_algo(self, text):
        items = self.algos[str(text)]
        self.search_combo.clear()
        self.search_combo.addItems(items)

    # switch maps tooltip in the destination_input input field
    def switch_maps_tooltip(self, text):
        items = self.map_tooltip[str(text)]
        str_items = "\n".join(items)
        tooltip_info = "MAP LOCATIONS \n\b {}".format(str_items)
        self.destination_input.setToolTip(tooltip_info)

    # get the algorithm code name
    def get_algo(self, algorithm=None):
        algorithm_dict = {'Depth First':'dfs', 'Breadth First':'bfs', 'Uniform Cost':'ucs',
                          'Greedy Best First': 'gbfs', 'A* Search': 'asts'}
        for i in range(len(algorithm_dict)):
            if algorithm == algorithm_dict.keys()[i]:
                algo = algorithm_dict.values()[i]
        return algo

    # algorithm to plot on canvas
    def plot(self):
        map = str(self.select_map_combo.currentText()).lower() # get selected map
        ubs_word = str(self.search_combo.currentText()) # name of the actual uninformed algorithm
        end = str(self.destination_input.text()) # name of goal
        dummy_runtime = np.random.randint(5,12) # represent with random numbers for now

        # get the algorithm's code
        algo = self.get_algo(algorithm=ubs_word)

        # call the graphing function
        numpath, x_capa, y_capa, x_capitula, y_capitula, labella = self.search.gui_target(map=map,
                                                                                          algorithm=algo,
                                                                                          goal=end)
        # set the items to be displayed at the bottom of the page
        self.disp_algorithm.setText('Algorithm: {}'.format(ubs_word))
        self.disp_start.setText('Start: Accra')
        self.disp_end.setText('End: {}'.format(end))
        self.disp_nodes_visited.setText('Nodes Visited: {}'.format(str(numpath)))
        self.disp_runtime.setText('Runtime: {}ms'.format(str(dummy_runtime)))

        # make an initial full subplot
        self.plt = self.figure.add_subplot(111)

        # clear the canvas to make way for a new plot
        self.plt.clear()

        # plot a scatter diagram of all the states in the tree
        self.plt.scatter([x_capa[x] for x in range(len(x_capa))],
                    [y_capa[y] for y in range(len(y_capa))],
                    marker='o')

        # # indicate respective labels on each node
        for label, x, y in zip(labella, x_capa, y_capa):
            self.plt.annotate(label, xy=(x, y))

        # plot the actual path returned by the search algorithm
        self.plt.plot([x_capitula[x] for x in range(len(x_capitula))],
                 [y_capitula[y] for y in range(len(y_capitula))])

        # activate graph grid
        self.plt.grid()

        # refresh canvas
        self.canvas.draw()

        # show default map on program start
    def default_plot(self):

        # call the graphing function
        numpath, x_capa, y_capa, x_capitula, y_capitula, labella = self.search.gui_target(map='original',
                                                                                          algorithm='ucs',
                                                                                              goal='Accra')
        # set the items to be displayed at the bottom of the page
        self.disp_algorithm.setText('Algorithm: None')
        self.disp_start.setText('Start: Accra')
        self.disp_end.setText('End: None')
        self.disp_nodes_visited.setText('Nodes Visited: None')
        self.disp_runtime.setText('Runtime: None')

        # make an initial full subplot
        self.plt = self.figure.add_subplot(111)

        # clear the canvas to make way for a new plot
        self.plt.clear()

        # plot a scatter diagram of all the states in the tree
        self.plt.scatter([x_capa[x] for x in range(len(x_capa))],
                         [y_capa[y] for y in range(len(y_capa))],
                         marker='o')

        # indicate respective labels on each node
        for label, x, y in zip(labella, x_capa, y_capa):
            self.plt.annotate(label, xy=(x, y))

        # plot the actual path returned by the search algorithm
        self.plt.plot([x_capitula[x] for x in range(len(x_capitula))],
                          [y_capitula[y] for y in range(len(y_capitula))])

        # activate graph grid
        self.plt.grid()

        # refresh canvas
        self.canvas.draw()

'''execute searcheron'''
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    # show splash screen
    splash_im = QtGui.QPixmap('sps.png')
    splash = QtGui.QSplashScreen(QtGui.QPixmap("sps.png"), QtCore.Qt.WindowStaysOnTopHint)
    progressbar = QtGui.QProgressBar(splash)
    # splash.setMask(splash_im.mask())
    splash.show()

    # progress bar
    for i in range(0, 100):
        progressbar.setValue(i)
        # cause a delay
        start = time.time()
        while time.time() < start + 0.1:
            # time.sleep(0.001)
            app.processEvents()

    main = Searcheron()
    main.show()
    splash.finish(main)
    sys.exit(app.exec_())
