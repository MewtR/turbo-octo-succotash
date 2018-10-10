import heapq
import heuristics
import utilities

def searchSPI(p):
    unvisited = []
    heapq.heappush(unvisited, (p.cost_so_far+heuristics.sum_of_permutation_inversion(p), p))
    visited = []

    while unvisited:
        current = heapq.heappop(unvisited)[1]
        with open('puzzleA_starSPITrace.txt', 'a') as f:
                f.write("{} {} cost = {}\n".format(current.move, current.config, current.cost_so_far))
        if utilities.goal(current):
            return current
        if utilities.wasVisited(current, visited):
            continue
        else: 
            children = utilities.generateChildren(current)
            #Remove visited children
            children = utilities.unvisitedChildren(children, visited)
            for c in children:
                heapq.heappush(unvisited, (c.cost_so_far+heuristics.sum_of_permutation_inversion(c), c))
            visited.append(current)
        #input("Press Enter to continue")
    return None


def searchMD(p):
    unvisited = []
    heapq.heappush(unvisited, (p.cost_so_far+heuristics.manhattan_distance(p), p))
    visited = []

    while unvisited:
        current = heapq.heappop(unvisited)[1]
        with open('puzzleA_starMDTrace.txt', 'a') as f:
                f.write("{} {} cost = {}\n".format(current.move, current.config, current.cost_so_far))
        if utilities.goal(current):
            return current
        if utilities.wasVisited(current, visited):
            continue
        else: 
            children = utilities.generateChildren(current)
            #Remove visited children
            children = utilities.unvisitedChildren(children, visited)
            for c in children:
                heapq.heappush(unvisited, (c.cost_so_far+heuristics.manhattan_distance(c), c))
            visited.append(current)
        #input("Press Enter to continue")
    return None
