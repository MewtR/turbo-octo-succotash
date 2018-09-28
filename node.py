class Node:
    def __init__(self, config, parent, move):
        self.config = config
        self.parent = parent
        self.move = move

    def __eq__(self, other):
        #Override the default Equals behavior
        if isinstance(other, self.__class__):
            return self.config == other.config
        return False

    def __ne__(self, other):
        #Override the default Unequal behavior
        return self.config != other.config
       
