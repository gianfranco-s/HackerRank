'''
Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?
'''

"""
P(B | A): probability of the occurrence of B given that A has occurred
P(B | A) = P(A and B) / P(A)

Bayes' Theroem: P(A | B) = P(B | A) · P(A) / P(B) = P(B | A) · P(A)/ ( P(B | A) · P(A) + P(B | A') · P(A') )


Abbreviations:
B: boy
G: girl

Probability of two children being boys given one of them is a boy: P(BB|B)

Possible events:
1. child_1 == B AND child_2 == B
2. child_1 == G AND child_2 == G
3. child_1 == B AND child_2 == G
4. child_1 == G AND child_2 == B

Given that one child has already been born, and it's a boy, event 2 can be discarded.

We're left with only THREE useful events, only one of which represents the current situation, that's why
P(BB|B) = 1/3

-- Another way:
P( 2 boys | 1 boy) = P(boy AND boy) / P(boy)
P = P_BB / P_B
"""
P_BB = 1/4  # Probability of getting two boys
P_B = 3/4   # Probability of getting one boy (favorable number / total number)
P = P_BB / P_B
print(P)