#Schur's Theorem

'''Schur's Theorem states that for any positive integer k, there exists a positive integer N such that any coloring of the integers 1, 2, ..., N with k colors contains a monochromatic solution to the equation a + b = c. We can use Python to find the smallest such N for a particular value of k. Here's an example:'''

def schur(k):
    N = 1
    while True:
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                s = i + j
                if s > N:
                    break
                for c in range(k):
                    if all(x in colors for x in (i, j, s)):
                        return N
        N += 1

print(schur(3))

#Expected Output: 14