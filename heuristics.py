from node import Node

def sum_of_permutation_inversion(p):
    value = 0 
    for x in range(11):
        for i in range(x+1, 12):
            if ((p.config[x] > p.config[i]) and p.config[i] != 0):
                value+=1
    return value





