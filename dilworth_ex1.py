#Dilworth's Theorem

#Dilworth's Theorem states that any finite partially ordered set can be partitioned into a minimum number of chains. We can use Python to find the size of the maximum antichain in a partially ordered set.

from itertools import combinations

def max_antichain_size(partial_order):
    n = len(partial_order)
    for k in range(n, 0, -1):
        for antichain in combinations(range(n), k):
            if all((i, j) not in partial_order for i, j in combinations(antichain, 2)):
                return k
    return 0

partial_order = [(0, 1), (1, 2), (2, 0), (2, 3)]
print(max_antichain_size(partial_order))


#Expected Output: 2

#This means that the largest antichain in the partially ordered set {(0, 1), (1, 2), (2, 0), (2, 3)} has size 2.