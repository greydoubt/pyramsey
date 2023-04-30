#Inclusion-Exclusion Principle

#The Inclusion-Exclusion Principle is a counting technique that allows us to count the number of elements in the union of finite sets. We can use Python to implement the Inclusion-Exclusion Principle for a particular example. 

def inclusion_exclusion_principle(n, sets):
    total = set(range(1, n+1))
    inclusion = sum((-1)**k * sum(len(set.intersection(*subset)) for subset in combinations(sets, k)) for k in range(len(sets)+1))
    return len(total) - inclusion

n = 20
sets = [{2, 3, 5, 7, 11, 13, 17}, {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}, or {4, 5, 6, 7, 12, 13, 14, 15, 20}]
print(inclusion_exclusion_principle(n, sets))


#Expected Output: 6

# This means that there are 6 numbers from 1 to 20 that belong to at least one of the sets {2, 3, 5, 7, 11, 13, 17}, {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}, or {4, 5, 6, 7, 12, 13, 14, 15, 20}.