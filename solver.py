from node import Node
import utilities
import depth_first
# Take puzzle in as input from user
# Split input by spaces and convert all elements to int
puzzle = [int(x) for x in input().split()]

root_node = Node(puzzle, None, '0')

#Example puzzles:
# 0 2 3 4 1 6 7 8 5 9 10 11 <- solved instantaneously
# 0 2 3 4 1 5 7 8 6 9 10 11 <- takes about 1 min to solve

print ("Is puzzle valid? "+str(utilities.valid(root_node)))
print ("Is puzzle in goal state? "+str(utilities.goal(root_node)))
goal_node = depth_first.search(root_node)
print ("------ Reached Goal State -------")
print ("Config:        "+str(goal_node.config))
print ("Parent config: "+str(goal_node.parent.config))
print ("Parent: "+str(goal_node.parent))
print ("Move: "+goal_node.move)

solution_path = utilities.find_solution_path(goal_node)
#print("Solution path is: "+str(solution_path))
#for x in solution_path:
#    print (x.move+"  "+str(x.config))
utilities.write_to_file(solution_path, 'puzzleDFS.txt')


#########Code commented out used for testing various functions ##################
#testVisited = generateChildren(root_node)
#testChildren = [Node([1, 2, 3, 4, 5, 6, 7, 0, 8, 9, 10, 11], root_node, 'x'),Node([1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 11], root_node, 'x')]
#for child in testChildren:
#    print ("Config:        "+str(child.config))
#testChildren = unvisitedChildren(testChildren, testVisited)
#print ("---------------------------------")
#for child in testChildren:
#    print ("Config:        "+str(child.config))

#testChildren = generateChildren(root_node)
#for child in testChildren:
#    print ("Parent config: "+str(child.parent.config))
#    print ("Config:        "+str(child.config))
#    print ("Parent: "+str(child.parent))
#    print ("Move: "+child.move)
#    print ("\n")
