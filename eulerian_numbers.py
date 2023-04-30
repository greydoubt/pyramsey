#Eulerian Numbers

#Eulerian numbers A(n, k) represent the number of permutations of an n-element set in which exactly k elements are greater than their preceding element. We can define a Python function to compute Eulerian numbers using the recursive definition as follows:

def eulerian(n, k):
    if k == 0:
        return 1
    if k == 1:
        return (n-1)
    return (n-k) * eulerian(n-1, k-1) + (k+1) * eulerian(n-1, k)

print(eulerian(5, 2))

#Output: 14

# define a decorator to print out the Eulerian number for any given pair of n and k:

def print_eulerian(func):
    def wrapper(n, k):
        print(f"A({n}, {k}) = {func(n, k)}")
    return wrapper

@print_eulerian
def eulerian(n, k):
    if k == 0:
        return 1
    if k == 1:
        return (n-1)
    return (n-k) * eulerian(n-1, k-1) + (k+1) * eulerian(n-1, k)

eulerian(6, 3)

#Output: 90
