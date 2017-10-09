try:
    from data_structs import Node
except ImportError:
    msg = "Unable to import Node package from data_structs"
    raise ImportError(msg)

__author__ = 'Biney Kingsley'

'''This class only handles all maps to be used in implementing the search algorithms'''


class Maps:

    def __init__(self, x_list=None, y_list = None, labels = None, tree = None):
        self.x_list = x_list
        self.y_list = y_list
        self.labels = labels
        self.tree = tree

    # empty list for plot coordinates and labels
    def reset(self):
        self.x_list = []
        self.y_list = []
        self.labels = []

    # create original map
    def original_map(self):
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

        return self.x_list, self.y_list, self.labels, self.tree

    # create extended map
    def extended_map(self):
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

        x = Node('Bubuashie', 20, 40)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert('Kaneshie', x, 'LEFT')

        x = Node('Tesano', 60, 20)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert('Bubuashie', x, 'RIGHT')

        x = Node('Mamprobi', 100, 80)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Dansoman", x, 'RIGHT')

        x = Node('Russia', 160, 80)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert('Mamprobi', x, 'RIGHT')

        x = Node('Korle Gono', 100, 40)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert('Mamprobi', x, 'LEFT')

        x = Node('James Town', 120, 20)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert('Korle Gono', x, 'RIGHT')

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

        x = Node('Cape Coast', 180, 200)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Mankessim", x, 'LEFT')

        x = Node('Elmina', 200, 160)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Cape Coast", x, 'RIGHT')

        x = Node('Kakum', 180, 100)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Elmina", x, 'LEFT')

        x = Node('Takoradi', 200, 40)
        self.x_list.append(x.get_x())
        self.y_list.append(x.get_y())
        self.labels.append(x.getKey())
        self.tree.insert("Elmina", x, 'RIGHT')

        return self.x_list, self.y_list, self.labels, self.tree