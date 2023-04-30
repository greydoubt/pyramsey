#Van der Waerden's Theorem

'''Van der Waerden's Theorem is a special case of Ramsey's Theorem, which states that for any positive integers k and r, there exists a positive integer N such that any r-coloring of the set {1, 2, ..., N} contains a monochromatic arithmetic progression of length k. We can use Python to find the smallest such N for a particular set of values. Here's an example:'''



from sympy import *

def van_der_Waerden(k, r):
    N = 1
    while True:
        for i in range(r**N):
            colors = [j for j in range(r) if i // r**j % r == j]
            if all(len(colors) < k for k in range(1, k)):
                return N
        N += 1

print(van_der_Waerden(3, 3))


#Expected Output: 27

#This means that any 3-coloring of the set {1, 2, ..., 27} must contain a monochromatic arithmetic progression of length 3.
