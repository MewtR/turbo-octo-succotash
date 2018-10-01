from node import Node
import utilities
import depth_first
import time
import heuristics
import best_first
# Take puzzle in as input from user
# Split input by spaces and convert all elements to int
puzzle = [int(x) for x in input().split()]

root_node = Node(puzzle, None, '0')

#Example puzzles:
#DFS
# 0 2 3 4 1 6 7 8 5 9 10 11 <- solved instantaneously
# 0 2 3 4 1 5 7 8 6 9 10 11 <- takes about 30 secs to solve

#BFS with sum of permutation of inversions
# 0 2 3 4 1 6 7 8 5 9 10 11 <- solved instantaneously
# 0 2 3 4 1 5 7 8 6 9 10 11 <- solved instantaneously

print ("Is puzzle valid? "+str(utilities.valid(root_node)))
print ("Is puzzle in goal state? "+str(utilities.goal(root_node)))
start_time = time.time()
goal_node = best_first.search(root_node)

solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleBFS.txt')

print ("Program execution time: {}".format(time.time()-start_time))

