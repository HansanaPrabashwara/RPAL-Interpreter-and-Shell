class Node:
    """Create Node instances to create tree data structure for parser tree 
    """
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.insert(0, child)

    def add_child_end(self, child):
        self.children.append(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
        else:
            print("Child not found")

    def __str__(self):
        return f" ({self.data} , {self.children}) " 
    
    def __repr__(self):
        return f" ({self.data} , {self.children}) " 