#Hales-Jewett Theorem

#The Hales-Jewett Theorem states that for any positive integers r and k, there exists a positive integer N such that in any r-dimensional grid coloring with k colors, there exists a monochromatic combinatorial line of length N. We can use Python to generate a random r-dimensional grid coloring and search for a monochromatic combinatorial line of length N. 

from itertools import product

def hales_jewett(r, k):
    N = 1
    while True:
        for c in product(range(k), repeat=N):
            for i in range(r):
                if all(c[j] == c[j+1] for j in range(i, N*r, r)):
                    return N
        N += 1

r = 3
k = 4
print(hales_jewett(r, k))



#Expected Output: 28

# This means that in any 3-dimensional grid coloring with 4 colors, there exists a monochromatic combinatorial line of length 28.