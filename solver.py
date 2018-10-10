from node import Node
import utilities
import depth_first
import time
import heuristics
import best_first
import a_star
# Take puzzle in as input from user
# Split input by spaces and convert all elements to int
puzzle = [int(x) for x in input().split()]

root_node = Node(puzzle, None, '0', 0)

#Example puzzles:
#DFS
# 0 2 3 4 1 6 7 8 5 9 10 11 <- solved instantaneously
# 0 2 3 4 1 5 7 8 6 9 10 11 <- takes about 30 secs to solve
# 9 0 6 1 3 10 8 11 2 5 7 4 <- ??? (way too long)

#BFS with sum of permutation of inversions
# 0 2 3 4 1 6 7 8 5 9 10 11 <- solved instantaneously
# 0 2 3 4 1 5 7 8 6 9 10 11 <- solved instantaneously
# 9 0 6 1 3 10 8 11 2 5 7 4 <- solved instantaneously

print ("Is puzzle valid? "+str(utilities.valid(root_node)))
print ("Is puzzle in goal state? "+str(utilities.goal(root_node)))
print ("Manhattan distance is: "+str(heuristics.manhattan_distance(root_node)))
#A*
#SPI
start_time = time.time()
goal_node = a_star.searchSPI(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleA_star.txt')
print ("Time to finish A* SPI: {}".format(time.time()-start_time))
#MD
start_time = time.time()
goal_node = a_star.searchMD(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleA_star.txt')
print ("Time to finish A* MD: {}".format(time.time()-start_time))
#BFS
#SPI
start_time = time.time()
goal_node = best_first.searchSPI(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleBFS-h1.txt')
print ("Time to finish BFS SPI: {}".format(time.time()-start_time))
goal_node = depth_first.search(root_node)
#MD
start_time = time.time()
goal_node = best_first.searchMD(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleBFS-h2.txt')
print ("Time to finish BFS MD: {}".format(time.time()-start_time))
goal_node = depth_first.search(root_node)
