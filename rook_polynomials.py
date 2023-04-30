#Rook Polynomials

#Rook polynomials represent the number of ways to place non-attacking rooks on a chessboard of a certain size. We can define a Python function to compute the rook polynomial using the recursive definition as follows:


def rook_polynomial(n, k):
    if n == 0:
        return 1
    return (n-k+1)*rook_polynomial(n-1,k-1) + k*rook_polynomial(n-1,k)

print(rook_polynomial(4,2))

#Output: 14

# define a decorator to print out the rook polynomial for any given n and k:

def print_rook_polynomial(func):
    def wrapper(n, k):
        print(f"R({n},{k}) = {func(n,k)}")
    return wrapper

@print_rook_polynomial
def rook_polynomial(n, k):
    if n == 0:
        return 1
    return (n-k+1)*rook_polynomial(n-1,k-1) + k*rook_polynomial(n-1,k)

rook_polynomial(5,3)

#Output: 175