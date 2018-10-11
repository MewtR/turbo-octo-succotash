from node import Node
import utilities

def search(p):
    unvisited = [p]
    visited = []

    while unvisited:
        current = unvisited.pop()
        with open('puzzleDFSTrace.txt', 'a') as f:
                f.write("{} {} \n".format(current.move, current.config))
        if utilities.goal(current):
            return current
        if utilities.wasVisited(current, visited):
            continue
        else: 
            children = utilities.generateChildren(current)
            #Remove visited children
            children = utilities.unvisitedChildren(children, visited)
            unvisited.extend(children)
            visited.append(current)
        #input("Press Enter to continue")
    return None
