

class Environment(object):
    """A class representing an environment.

    Args:
        number (int): The number associated with the environment.
        parent (object): The parent object of the environment.

    Attributes:
        name (str): The name of the environment.
        variables (dict): A dictionary of variables in the environment.
        children (list): A list of child nodes of the environment.
        parent (object): The parent object of the environment.
    """
    def __init__(self, number, parent):
        self.name = "e_" + str(number)
        self.variables = {}
        self.children = []
        self.parent = parent

    def add_child(self, child_env):
        """Add a child node to the environment.

        Args:
            node (object): The child node to be added.
        """
        self.children.append(child_env)
        child_env.variables.update(self.variables)

    def add_variable(self, key, value):
        """Add a variable to the environment.

        Args:
            key: The key of the variable.
            value: The value of the variable.
        """
        self.variables[key] = value

    def __str__(self) -> str:
        """Return a string representation of the environment.

        Returns:
            str: The string representation of the environment.
        """
        return f"{self.name}[{self.variables}]"
    
    def __repr__(self) -> str:
        """Return a string representation of the environment.

        Returns:
            str: The string representation of the environment.
        """
        return f"Tau_{self.size}"