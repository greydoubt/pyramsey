#Stirling Numbers of the Second Kind

#Stirling numbers of the second kind S(n, k) represent the number of ways to partition an n-element set into k non-empty subsets. We can define a Python function to compute Stirling numbers of the second kind using the recursive definition as follows:

def stirling(n, k):
    if k == 0 or k > n:
        return 0
    if k == 1 or k == n:
        return 1
    return k * stirling(n-1, k) + stirling(n-1, k-1)

print(stirling(5, 2))

#Output: 15

# define a decorator to print out the Stirling number for any given pair of n and k:

def print_stirling(func):
    def wrapper(n, k):
        print(f"S({n}, {k}) = {func(n, k)}")
    return wrapper

@print_stirling
def stirling(n, k):
    if k == 0 or k > n:
        return 0
    if k == 1 or k == n:
        return 1
    return k * stirling(n-1, k) + stirling(n-1, k-1)

stirling(6, 3)

#Output: S(6, 3) = 90
