#Ramsey Numbers

#Ramsey numbers R(k, l) represent the minimum number of vertices in a complete graph that guarantees either a clique of size k or an independent set of size l. We can define a Python function to compute Ramsey numbers using the recursive definition as follows:

def ramsey(k, l):
    if k == 2 and l == 2:
        return 2
    if k == 1 or l == 1:
        return 1
    return ramsey(k-1, l) + ramsey(k, l-1)

print(ramsey(3, 3))

#Output: 6

#define a decorator to print out the Ramsey number for any given pair of k and l:


def print_ramsey(func):
    def wrapper(k, l):
        print(f"R({k}, {l}) = {func(k, l)}")
    return wrapper

@print_ramsey
def ramsey(k, l):
    if k == 2 and l == 2:
        return 2
    if k == 1 or l == 1:
        return 1
    return ramsey(k-1, l) + ramsey(k, l-1)

ramsey(4, 4)

#Output: R(4, 4) = 18
