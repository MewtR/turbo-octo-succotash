import heapq
import heuristics
import utilities

def search(p):
    unvisited = []
    heapq.heappush(unvisited, (heuristics.sum_of_permutation_inversion(p), p))
    visited = []

    while unvisited:
        current = heapq.heappop(unvisited)[1]
        #with open('puzzleBFS.txt', 'a') as f:
        #        f.write("{} {} SPI= {}\n".format(current.move, current.config, heuristics.sum_of_permutation_inversion(current)))

        if utilities.goal(current):
            return current
        if utilities.wasVisited(current, visited):
            continue
        else: 
            children = utilities.generateChildren(current)
            #Remove visited children
            children = utilities.unvisitedChildren(children, visited)
            for c in children:
                heapq.heappush(unvisited, (heuristics.sum_of_permutation_inversion(c), c))
            visited.append(current)
        #input("Press Enter to continue")
    return None


