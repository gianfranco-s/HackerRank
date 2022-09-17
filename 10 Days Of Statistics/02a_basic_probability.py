'''
Task
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.
'''

"""
------------------------ First, let's try to solve an easier one -------------------------
# Find the probability of getting 1 head and 1 tail when 2 fair coins are tossed.

# Possible outcomes for each toss
S1 = {'H', 'T'}
S2 = {'H', 'T'}

# All possible outcomes: S = S1 x S2 (Cartesian Product)
S = set()
for i in S1:
    for j in S2:
        S.add((i, j))
# S = {('H', 'H'), ('H', 'T'), ('T', 'H'), ('T', 'T')}

# Favorable outcomes
A = {('H', 'T'), ('T', 'H')}

# P(getting H and T) = len(A)/len(S)
P = len(A)/len(S)
print(P)

#------------------------------------------------------------------------------------------
"""

# Possible outcomes for each dice roll
S1 = {1, 2, 3, 4, 5 ,6}
S2 = {1, 2, 3, 4, 5 ,6}

# All possible outcomes: S = S1 x S2 (Cartesian Product)
S = set()
for i in S1:
    for j in S2:
        S.add((i, j))

# Favorable outcomes would be all possible outcomes, minus the outcomes where sum is over 9
# That would be when the sum is 10, 11 or 12
B = {(5, 5), (5, 6), (6, 5), (6, 6), (4, 6), (6, 4)}  # Instances where sum of elems is over 9 (I got this manually)
A = S - B

B_calculated = set()
for i in S1:
    for j in S2:
        if i + j > 9:
            B_calculated.add((i, j))

print(f'Both methods to get B are correct: B == B_calculated --> {B == B_calculated}')

# Overall probability:
P = len(A)/len(S)
print(P)

