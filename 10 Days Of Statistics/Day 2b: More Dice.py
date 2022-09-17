'''
In a single toss of 2 fair (evenly-weighted) six-sided dice,
find the probability that 
- the values rolled by each die will be different
- and the two dice have a sum of 6.
'''

# Possible outcomes for each dice roll
S1 = {1, 2, 3, 4, 5 ,6}
S2 = {1, 2, 3, 4, 5 ,6}

# All possible outcomes: S = S1 x S2 (Cartesian Product)
S = set((i, j) for i in S1 for j in S2)


# event A1: values rolled are different:
# With comprehension: A1_comp = set((i, j) for i in S1 for j in S2 if i != j)

A1 = set()
for i in S1:
    for j in S2:
        if i != j:
            A1.add((i, j))

# However, A2 pairs must have different values... so I'll just remove duplicated values from A1:
A2 = set(elem for elem in A1 if elem[0] + elem[1] == 6)

# There must be a mathy way to solve this... Oh well, I'll cross that bridge when I need to.

P = len(A2)/len(S)
print(P)