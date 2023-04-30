#Binomial Coefficients

#The binomial coefficient n choose k, denoted as C(n,k), gives the number of ways to choose k elements from a set of n elements. We can define a Python function to compute the binomial coefficient recursively as follows:


def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)


def print_binomial(func):
    def wrapper(n, k):
        print(f"C({n}, {k}) = {func(n, k)}")
    return wrapper

@print_binomial
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

binomial(5, 2)

#Output: C(5, 2) = 10
