#Narayana Numbers

#Narayana numbers N(n,k) represent the number of ways to rearrange the elements of a cyclic sequence of n elements with k pairs of adjacent elements swapped. We can define a Python function to compute Narayana numbers using the recursive definition as follows:


def narayana(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n-1
    return ((n-1)*narayana(n-1, k) + (k-1)*narayana(n-1, k-1))

print(narayana(5, 2))

#Output: 7

# define a decorator to print out the Narayana number for any given n and k:

def print_narayana(func):
    def wrapper(n, k):
        print(f"N({n},{k}) = {func(n,k)}")
    return wrapper

@print_narayana
def narayana(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n-1
    return ((n-1)*narayana(n-1, k) + (k-1)*narayana(n-1, k-1))

narayana(6, 3)

#Output: 70
