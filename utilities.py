from node import Node
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

    for x in range(1, 12):
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
    #if blank is at index 8 it can't go up left
    if ((zero_index - 5 > -1) and (zero_index != 8)) :
        up_left_index = zero_index-5
        up_left_child = p.config.copy()
        up_left_child = swap(up_left_child, up_left_index, zero_index)
        children.append(Node(up_left_child, p, chr(up_left_index+97), p.cost_so_far+1))
    #Up index-4 is tile above tile at index
    if (zero_index - 4 > -1):
        up_index = zero_index-4
        up_child = p.config.copy()
        up_child = swap(up_child, up_index, zero_index)
        children.append(Node(up_child, p, chr(up_index+97), p.cost_so_far+1))
    #Up right is index - 3
    # if blank at index 3, 7 or 11, can't go up right
    if ((zero_index - 3 > 0) and ((zero_index-3) % 4 != 0)):
        up_right_index = zero_index-3
        up_right_child = p.config.copy()
        up_right_child = swap(up_right_child, up_right_index, zero_index)
        children.append(Node(up_right_child, p, chr(up_right_index+97), p.cost_so_far+1))
    #Left is index-1
    #indices 0, 4 and 8 can't go left
    if ((zero_index % 4 != 0)):
        left_index = zero_index-1
        left_child = p.config.copy()
        left_child = swap(left_child, left_index, zero_index)
        children.append(Node(left_child, p, chr(left_index+97), p.cost_so_far+1))
    #Right is index+1
    #indices 3, 7 and 11 can't go right
    if ((zero_index % 4 != 3)):
        right_index = zero_index+1
        right_child = p.config.copy()
        right_child = swap(right_child, right_index, zero_index)
        children.append(Node(right_child, p, chr(right_index+97), p.cost_so_far+1))
    #Down left is index+3
    if ((zero_index + 3 < 11) and (zero_index % 4 != 0 )):
        down_left_index = zero_index+3
        down_left_child = p.config.copy()
        down_left_child = swap(down_left_child, down_left_index, zero_index)
        children.append(Node(down_left_child, p, chr(down_left_index+97), p.cost_so_far+1))
    #Down right is index+5
    #indices 3, 7 and 11 can't go down right
    if ((zero_index + 5 < 12) and (zero_index != 3)):
        down_right_index = zero_index+5
        down_right_child = p.config.copy()
        down_right_child = swap(down_right_child, down_right_index, zero_index)
        children.append(Node(down_right_child, p, chr(down_right_index+97), p.cost_so_far+1))
    #Down is index+4
    if ((zero_index + 4 < 12)):
        down_index = zero_index+4
        down_child = p.config.copy()
        down_child = swap(down_child, down_index, zero_index)
        children.append(Node(down_child, p, chr(down_index+97), p.cost_so_far+1))

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

def find_solution_path(goal_node):
    solution = []
    while (goal_node.parent):
        solution.append(goal_node)
        goal_node = goal_node.parent
    solution.append(goal_node)
    solution.reverse()
    return solution

def write_to_file(solution_path, file_name):
    with open(file_name, 'w') as f:
        for x in solution_path:
            f.write("{} {} cost: {}\n".format(x.move,x.config, x.cost_so_far))
