from Interpreter.CSComponents import Lambda, Delta, Tau
from copy import deepcopy

class ControlSuctureBuilder:
    """A class that builds control structures based on a given ST.

    Attributes:
        ST (Node): The SI_Tree object representing the syntax tree.
        control_structures (list): A list to store the control structures.
        count (int): A counter to keep track of the control structure count.
    """

    def __init__(self, SI_Tree):
        self.ST = SI_Tree
        self.control_structures = []
        self.count = 0

    def linerize(self):
        self.pre_order(self.ST, 0)
        return self.control_structures
    
    def printCS(self):
            """
            Prints the control structures.

            """
            self.pre_order(self.ST, 0)
            cs = deepcopy(self.control_structures)
            for i in range(len(cs)): 
                for j in range(len(cs[i])):
                    if cs[i][j] == "gamma":
                        cs[i][j] = "\u03B3"
            for i in range(len(cs)):
                print(f"\u03B4_{i} : {cs[i]}")

    def pre_order(self, root, index):
        """Traverses the syntax tree in pre-order and builds the control structures.

        Args:
            root: The current node being visited.
            index (int): The index of the control structure list.

        Returns:
            None
        """
        # if the amount of control structures are lower than the index, add more until it equals the index
        if len(self.control_structures) <= index:
            self.control_structures.append([])
        # If the node is lambda handle it
        if root.data == "lambda":
            self.count += 1
            if root.children[0].data == ",":
                cs = Lambda(self.count)
                val = []
                for node in root.children[0].children:
                    val.append(node.data)
                cs.val = val
                self.control_structures[index].append(cs) 
            else:
                cs = Lambda(self.count,root.children[0].data)
                self.control_structures[index].append(cs)

            for node in root.children[1:]:
                self.pre_order(node, self.count)
        # If the root data is -> add delta then delta else and beta to the control structure
        elif root.data == "->":
            self.count += 1
            cs = Delta(self.count)
            self.control_structures[index].append(cs)
            self.pre_order(root.children[1], self.count)
            self.count += 1
            cs = Delta(self.count)
            self.control_structures[index].append(cs)
            self.pre_order(root.children[2], self.count)
            self.control_structures[index].append("beta")
            self.pre_order(root.children[0], index)
        
        # If the root data is tau add Tau object including the tuple size to the control structure
        elif(root.data == "tau"):
            n = len(root.children)
            cs = Tau(n)
            self.control_structures[index].append(cs)
            for node in root.children:
                self.pre_order(node, index)
        
        # If it is something else add data data to the control structure.
        else:
            self.control_structures[index].append(root.data)
            for node in root.children:
                self.pre_order(node, index)

