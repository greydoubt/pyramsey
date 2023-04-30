#Combinatorial Numbers

#Combinatorial numbers C(n, k) represent the number of k-element subsets of an n-element set. We can define a Python function to compute combinatorial numbers using the recursive definition as follows:

def comb(n, k):
    if k == 0 or k == n:
        return 1
    return comb(n-1, k-1) + comb(n-1, k)

print(comb(5, 2))

# Output: 10

#define a decorator to print out the combinatorial number for any given pair of n and k:


def print_comb(func):
    def wrapper(n, k):
        print(f"C({n}, {k}) = {func(n, k)}")
    return wrapper

@print_comb
def comb(n, k):
    if k == 0 or k == n:
        return 1
    return comb(n-1, k-1) + comb(n-1, k)

comb(6, 3)

#Output: C(6, 3) = 20
