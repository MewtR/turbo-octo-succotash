from node import Node

def sum_of_permutation_inversion(p):
    value = 0 
    for x in range(11):
        for i in range(x+1, 12):
            if p.config[x] == 0:
                continue
            if ((p.config[x] > p.config[i]) and p.config[i] != 0):
                value+=1
    return value

def manhattan_distance(p):
    value = 0
    for x in range(0,12):
        start = x
        if p.config[x] == 0:
            #end = 11
            continue
        else:
            end = p.config[x]-1
        stepEWV = stepEW(start,end)
        stepNSV = stepNS(start,end)
        #Allow diagonal moves
        if (stepEWV >= stepNSV):
            value+=stepEWV
        else: 
            value+=stepNSV
        #value+= stepEW(start,end) + stepNS(start,end)
    return value
        
        
def stepNS(start, end):
    return abs((start//4) - (end//4))


def stepEW(start, end):
    return abs((start % 4) - (end % 4))

def hamming_distance(p):
    value = 0
    for x in range(12):
        if p.config[x] == 0:
            continue
        if p.config[x] != x+1:
            value+=1
    return value
