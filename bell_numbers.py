#Bell Numbers

#Bell numbers B(n) represent the number of ways to partition an n-element set. We can define a Python function to compute Bell numbers using the recursive definition as follows:

def bell(n):
    if n == 0:
        return 1
    sum = 0
    for k in range(1, n+1):
        sum += comb(n-1, k-1) * bell(n-k)
    return sum

print(bell(5))

#Output: 52

#define a decorator to print out the Bell number for any given n:

def print_bell(func):
    def wrapper(n):
        print(f"B({n}) = {func(n)}")
    return wrapper

@print_bell
def bell(n):
    if n == 0:
        return 1
    sum = 0
    for k in range(1, n+1):
        sum += comb(n-1, k-1) * bell(n-k)
    return sum

bell(6)

#Output: B(6) = 203
