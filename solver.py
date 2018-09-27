# Take puzzle in as input from user
# Split input by spaces and convert all elements to int
puzzle = [int(x) for x in input().split()]

print (puzzle)

# Checks if puzzle is valid ie contains 0 up to 11
def valid(p):
    if (len(p) != 12):
        return False
    else:
        for x in range(12):
            if x not in p:
                return False
        return True

# Checks if puzzle is in goal state
def goal(p):
    for x in range(1, 11):
        if p[x-1] != x:
            return False
    return True

print ("Is puzzle valid? "+str(valid(puzzle)))
print ("Is puzzle in goal state? "+str(goal(puzzle)))

