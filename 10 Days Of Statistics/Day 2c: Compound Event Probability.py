'''
There are 3 urns labeled X, Y, and Z.

- Urn X contains 4 red balls and 3 black balls.
- Urn Y contains 5 red balls and 4 black balls.
- Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?
'''


# Possible outcomes for a draw from each urn: each urn has either red or black balls
SX = ('r', 'r', 'r', 'r', 'b', 'b', 'b')
SY = ('r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b')
SZ = ('r', 'r', 'r', 'r', 'b', 'b', 'b', 'b',)

# The probability of getting a specific color from each urn, is different:
PX_r = SX.count('r')/len(SX)
PX_b = SX.count('b')/len(SX)

PY_r = SY.count('r')/len(SY)
PY_b = SY.count('b')/len(SY)

PZ_r = SZ.count('r')/len(SZ)
PZ_b = SZ.count('b')/len(SZ)

# Possible cases
# 1. Take ['r' from X] AND take  ['r' from Y] AND take ['b' from Z]
case_1 = PX_r * PY_r * PZ_b

# 2. Take ['r' from X] AND take  ['b' from Y] AND take ['r' from Z]
case_2 = PX_r * PY_b * PZ_r

# 3. Take ['b' from X] AND take  ['r' from Y] AND take ['r' from Z]
case_3 = PX_b * PY_r * PZ_r

# Since the total probability is either case, we should use OR to calculate the final probability
P = case_1 + case_2 + case_3
print(P)

# -------------------------------- A more condensed code -----------------------------
PX = { 'red': 4/7, 'black': 3/7 }
PY = { 'red': 5/9, 'black': 4/9 }
PZ = { 'red': 4/8, 'black': 4/8 }

first_case = PX['red'] * PY['red'] * PZ['black']
second_case = PX['red'] * PY['black'] * PZ['red']
third_case = PX['black'] * PY['red'] * PZ['red']
print(first_case + second_case + third_case)