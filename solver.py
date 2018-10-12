from node import Node
import utilities
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
# 1 0 3 7 5 2 6 4 9 10 11 8 <- puzzle from handout

#print ("Is puzzle valid? "+str(utilities.valid(root_node)))
#print ("Is puzzle in goal state? "+str(utilities.goal(root_node)))
#print ("Manhattan distance: "+str(heuristics.manhattan_distance(root_node)))
#print ("SPI: "+str(heuristics.sum_of_permutation_inversion(root_node)))
#print ("Hamming distance: "+str(heuristics.hamming_distance(root_node)))
#BFS
#HD
start_time = time.time()
goal_node = best_first.searchHD(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleBFS-h1.txt')
print ("Time to finish BFS hamming distance: {}".format(time.time()-start_time))
#MD
start_time = time.time()
goal_node = best_first.searchMD(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleBFS-h2.txt')
print ("Time to finish BFS Manhattan distance: {}".format(time.time()-start_time))
#A*
#SPI
#start_time = time.time()
#goal_node = a_star.searchSPI(root_node)
#solution_path = utilities.find_solution_path(goal_node)
#utilities.write_to_file(solution_path, 'puzzleAs-h1.txt')
#print ("Time to finish A* SPI: {}".format(time.time()-start_time))
#HD
start_time = time.time()
goal_node = a_star.searchHD(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleAs-h1.txt')
print ("Time to finish A* hamming distance: {}".format(time.time()-start_time))
#MD
start_time = time.time()
goal_node = a_star.searchMD(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleAs-h2.txt')
print ("Time to finish A* Manhattan distance: {}".format(time.time()-start_time))
start_time = time.time()
