from typing import List


import random

def ListShuffle(list):
    l = list
    for i in range(len(l) - 1):
        p1 = random.randrange(0,(len(l)))
        p2 = random.randrange(0,(len(l)))
        l1 = l[p1]
        l[p1] = l[p2]
        l[p2] = l1