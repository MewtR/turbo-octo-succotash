from node import Node
# Take puzzle in as input from user
# Split input by spaces and convert all elements to int
puzzle = [int(x) for x in input().split()]

root_node = Node(puzzle, None, '0')

#print (puzzle)
#print (root_node.config)
#print (root_node.parent)
#print (root_node.move)

# Checks if puzzle is valid ie contains 0 up to 11
def valid(p):
    if (len(p.config) != 12):
        return False
    else:
        for x in range(12):
            if x not in p.config:
                return False
        return True

# Checks if puzzle is in goal state
def goal(p):
    if not valid(p):
        return False

    for x in range(1, 11):
        if p.config[x-1] != x:
            return False
    return True


def swap(l, x, y):
    l[x], l[y] = l[y], l[x]
    return l


def generateChildren(p):
    children = []
    zero_index = p.config.index(0)
    #Up left is index - 5
    if (zero_index - 5 > -1) :
        up_left_index = zero_index-5
        up_left_child = p.config.copy()
        up_left_child = swap(up_left_child, up_left_index, zero_index)
        children.append(Node(up_left_child, p, chr(up_left_index+97)))
    #Up index-4 is tile above tile at index
    if (zero_index - 4 > -1):
        up_index = zero_index-4
        up_child = p.config.copy()
        up_child = swap(up_child, up_index, zero_index)
        children.append(Node(up_child, p, chr(up_index+97)))
    #Up right is index - 3
    if ((zero_index - 3 > 0) and ((zero_index-3) % 4 != 0)):
        up_right_index = zero_index-3
        up_right_child = p.config.copy()
        up_right_child = swap(up_right_child, up_right_index, zero_index)
        children.append(Node(up_right_child, p, chr(up_right_index+97)))
    #Left is index-1
    if ((zero_index % 4 != 0)):
        left_index = zero_index-1
        left_child = p.config.copy()
        left_child = swap(left_child, left_index, zero_index)
        children.append(Node(left_child, p, chr(left_index+97)))
    #Right is index+1
    if ((zero_index % 4 != 3)):
        right_index = zero_index+1
        right_child = p.config.copy()
        right_child = swap(right_child, right_index, zero_index)
        children.append(Node(right_child, p, chr(right_index+97)))
    #Down left is index+3
    if ((zero_index + 3 < 11) and (zero_index % 4 != 0 )):
        down_left_index = zero_index+3
        down_left_child = p.config.copy()
        down_left_child = swap(down_left_child, down_left_index, zero_index)
        children.append(Node(down_left_child, p, chr(down_left_index+97)))
    #Down right is index+5
    if ((zero_index + 5 < 12)):
        down_right_index = zero_index+5
        down_right_child = p.config.copy()
        down_right_child = swap(down_right_child, down_right_index, zero_index)
        children.append(Node(down_right_child, p, chr(down_right_index+97)))
    #Down is index+4
    if ((zero_index + 4 < 12)):
        down_index = zero_index+4
        down_child = p.config.copy()
        down_child = swap(down_child, down_index, zero_index)
        children.append(Node(down_child, p, chr(down_index+97)))

    return children

def wasVisited(p, visited):
    for x in visited:
        if p == x:
            return True
    return False

#After generating children
#We must remove those that have already been visited
#or we can get stuck in an infinite loop
def unvisitedChildren(children, visited):
    if visited:
        visitedConfigs = [v.config for v in visited]
        children = [c for c in children if c.config not in visitedConfigs]
        return children
    else:
        return children


def depth_first_search(p):
    unvisited = [p]
    visited = []

    while unvisited:
        current = unvisited.pop()
        if current.parent:
            print ("Parent config: "+str(current.parent.config))
        print ("Config:        "+str(current.config))
        print ("Move: "+current.move)
        print ("\n")
        if goal(current):
            return current
        if wasVisited(current, visited):
            continue
        else: 
            children = generateChildren(current)
            #Remove visited children
            children = unvisitedChildren(children, visited)
            unvisited.extend(children)
            visited.append(current)
        #input("Press Enter to continue")
    return None




print ("Is puzzle valid? "+str(valid(root_node)))
print ("Is puzzle in goal state? "+str(goal(root_node)))
goal_node = depth_first_search(root_node)
print ("------ Reached Goal State -------")
print ("Config:        "+str(goal_state.config))
print ("Parent config: "+str(goal_state.parent.config))
print ("Parent: "+str(goal_state.parent))
print ("Move: "+goal_state.move)

#########Code commented out used for testing various functions ##################
#testVisited = generateChildren(root_node)
#testChildren = [Node([1, 2, 3, 4, 5, 6, 7, 0, 8, 9, 10, 11], root_node, 'x'),Node([1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 11], root_node, 'x')]
#for child in testChildren:
#    print ("Config:        "+str(child.config))
#testChildren = unvisitedChildren(testChildren, testVisited)
#print ("---------------------------------")
#for child in testChildren:
#    print ("Config:        "+str(child.config))

#for child in testChildren:
#    print ("Config:        "+str(child.config))
#    print ("Parent config: "+str(child.parent.config))
#    print ("Parent: "+str(child.parent))
#    print ("Move: "+child.move)
#    print ("Is parent equal to child? "+ str(child == root_node))
#    print ("\n")
