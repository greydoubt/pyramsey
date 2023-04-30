#Schröder Numbers

#Schröder numbers S(n) represent the number of ways to insert parentheses in a sequence of n+1 items such that it forms a valid expression. We can define a Python function to compute Schröder numbers using the recursive definition as follows:

def schroder(n):
    if n == 0:
        return 1
    return schroder(n-1) + sum(schroder(i)*schroder(n-1-i) for i in range(n-1))

print(schroder(4))

#Output: 14

# define a decorator to print out the Schröder number for any given n:


def print_schroder(func):
    def wrapper(n):
        print(f"S({n}) = {func(n)}")
    return wrapper

@print_schroder
def schroder(n):
    if n == 0:
        return 1
    return schroder(n-1) + sum(schroder(i)*schroder(n-1-i) for i in range(n-1))

schroder(5)

#Output: 42
