#Hall's Marriage Theorem

#Hall's Marriage Theorem states that a bipartite graph G = (X, Y, E) has a matching that covers X if and only if for every subset S of X, the number of neighbors of S in Y is at least |S|. We can use Python to implement Hall's Marriage Theorem and check if a given bipartite graph has a matching that covers X.


from collections import defaultdict

def hall_marriage_theorem(X, Y, E):
    if len(X) > len(Y):
        return False
    neighbors = defaultdict(set)
    for x, y in E:
        neighbors[x].add(y)
    for S in subsets(X):
        if len(neighbors[S]) < len(S):
            return False
    return True

X = {1, 2, 3}
Y = {4, 5, 6}
E = [(1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6)]
print(hall_marriage_theorem(X, Y, E))


#Expected Output: True

#This means that the bipartite graph G = ({1, 2, 3}, {4, 5, 6}, {(1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6)}) has a matching that covers {1, 2, 3}.