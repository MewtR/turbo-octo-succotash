class Node:
    def __init__(self, config, parent, move, cost_so_far):
        self.config = config
        self.parent = parent
        self.move = move
        #Used for A* algorithm only
        self.cost_so_far = cost_so_far

    def __eq__(self, other):
        #Override the default Equals behavior
        if isinstance(other, self.__class__):
            return self.config == other.config
        return False

    def __ne__(self, other):
        #Override the default Unequal behavior
        return self.config != other.config

    #In case there is a tie during heapq operations
    def __lt__(self, other):
        return ord(self.move) < ord(other.move)
       
