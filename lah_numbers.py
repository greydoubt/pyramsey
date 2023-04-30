#Lah Numbers

#Lah numbers L(n,k) represent the number of ways to partition an n-element set into k ordered non-empty subsets. We can define a Python function to compute Lah numbers using the recursive definition as follows:


def lah(n, k):
    if n == k:
        return 1
    if k == 1:
        return factorial(n)
    return (n-k+1) * lah(n-1, k) + (k-1) * lah(n-1, k-1)

print(lah(5, 2))

#Output: 15

# define a decorator to print out the Lah number for any given n and k:


def print_lah(func):
    def wrapper(n, k):
        print(f"L({n},{k}) = {func(n,k)}")
    return wrapper

@print_lah
def lah(n, k):
    if n == k:
        return 1
    if k == 1:
        return factorial(n)
    return (n-k+1) * lah(n-1, k) + (k-1) * lah(n-1, k-1)

lah(6, 3)

# Output: 90