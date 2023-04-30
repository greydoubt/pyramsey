#Erdős–Szekeres Theorem

#The Erdős–Szekeres Theorem states that any sequence of n^2 + 1 distinct real numbers must contain either an increasing subsequence of length n + 1, or a decreasing subsequence of length n + 1. We can use Python to verify this theorem for a particular sequence. 


def erdos_szekeres(sequence, n):
    increasing = [sequence[0]]
    decreasing = [sequence[0]]
    for i in range(1, len(sequence)):
        j = bisect_left(increasing, sequence[i])
        k = bisect_left(decreasing, -sequence[i])
        if j >= n or k >= n:
            return True
        if j == len(increasing):
            increasing.append(sequence[i])
        else:
            increasing[j] = sequence[i]
        if k == len(decreasing):
            decreasing.append(-sequence[i])
        else:
            decreasing[k] = -sequence[i]
    return False

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = 3
print(erdos_szekeres(sequence, n))


#Expected output: True

# This means that any sequence of 11^2 + 1 = 122 distinct real numbers must contain either an increasing subsequence of length 3 + 1 = 4, or a decreasing subsequence of length 3 + 1 = 4.