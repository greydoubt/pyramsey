#Catalan Numbers

#Catalan numbers Cn represent the number of ways to arrange n pairs of parentheses such that they are all properly matched. We can define a Python function to compute Catalan numbers using the recursive definition as follows:

def catalan(n):
    if n == 0:
        return 1
    sum = 0
    for k in range(1, n+1):
        sum += catalan(k-1) * catalan(n-k)
    return sum

print(catalan(5))

#Output: 42

# define a decorator to print out the Catalan number for any given n:


def print_catalan(func):
    def wrapper(n):
        print(f"C({n}) = {func(n)}")
    return wrapper

@print_catalan
def catalan(n):
    if n == 0:
        return 1
    sum = 0
    for k in range(1, n+1):
        sum += catalan(k-1) * catalan(n-k)
    return sum

catalan(6)

#Output: C(6) = 132
