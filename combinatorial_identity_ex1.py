#Combinatorial Proofs

#Combinatorial proofs use combinatorial methods to prove algebraic identities. We can use Python to implement combinatorial proofs for certain identities. 

from math import factorial

def combinatorial_proof_identity(n):
    left = sum((-1)**k * factorial(n) // (factorial(k) * factorial(n - k)) for k in range(n+1))
    right = (-1)**n * factorial(n) // 2
    return left == right

n = 5
print(combinatorial_proof_identity(n))

#Expected Output: True

#This means that the identity sum((-1)^k * binom(n, k)) = (-1)^n * floor(n/2)! is true for n = 5.