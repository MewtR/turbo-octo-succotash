from node import Node
import utilities
import time
import depth_first
# Take puzzle in as input from user
# Split input by spaces and convert all elements to int
puzzle = [int(x) for x in input().split()]

root_node = Node(puzzle, None, '0', 0)

#DFS
start_time = time.time()
goal_node = depth_first.search(root_node)
solution_path = utilities.find_solution_path(goal_node)
utilities.write_to_file(solution_path, 'puzzleDFS.txt')
print ("Time to finish DFS: {}".format(time.time()-start_time))
