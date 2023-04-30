#Factorial Numbers

#Factorial numbers n! represent the product of all positive integers from 1 to n. We can define a Python function to compute factorial numbers using the recursive definition as follows:

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

#Output: 120

#define a decorator to print out the factorial number for any given n:
def print_fact(func):
    def wrapper(n):
        print(f"{n}! = {func(n)}")
    return wrapper

@print_fact
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

fact(6)

#Output: 6! = 720