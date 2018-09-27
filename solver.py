

# Take puzzle in as input from user
# Split input by spaces and convert all elements to int
puzzle = [int(x) for x in input().split()]

print (puzzle)

def valid(p):
    if (len(p) != 12):
        return False
    else:
        for x in range(12):
            if x not in p:
                return False
        return True

print ("Is puzzle valid? "+str(valid(puzzle)))
