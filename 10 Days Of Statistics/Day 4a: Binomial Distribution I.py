'''
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion 
of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).
'''

from math import factorial

def cumulative_binomial(modifier, r, n, p):
    comb = lambda n, r: factorial(n) / ( factorial(r) * factorial(n - r) )
    binom_distrib = lambda x, n, p: comb(n, x) * (p**x) * (1-p)**(n-x)
    sum_limits = {
        'at least': (r, n+1),
        'at most': (0, r+1),
    }.get(modifier)
    return sum([binom_distrib(i, n, p) for i in range(*sum_limits)])

# boys = 1.09
# girls = 1
boys, girls = map(float, input().split())

r = 3                                               # Number of desired successes
n = 6                                               # Number of trials. In this case, amount of total babies
p = boys/(boys+girls)                               # Probability of success after 1 trial
P_total = cumulative_binomial('at least', r, n, p)  # Total probability

print(round(P_total, 3))