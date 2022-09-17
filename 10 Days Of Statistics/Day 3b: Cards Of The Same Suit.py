'''
You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?
'''

# We only need to compute the probability of the second event
# The first card determines the suit. Of that specific suit, only 12 cards remain, in now a 51-card deck.
# So P = 12/51

# Let's find a coded approach:
def combination(total, sample):
    n = total
    r = sample
    return factorial(n) / ( factorial(r) * factorial(n - r) )

# My definition of factorial() doesn't work because of int numbers max cap
# def factorial(n):
#     assert n > 0, 'n should be an integer number or zero'
#     return 1 if (n == 0 or n == 1) else n * (n - 1)
from math import factorial

drawing_two_from_full_deck = combination(52, 2)
drawing_two_from_same_suit = combination(13, 2)
drawing_two_from_same_suit_total = 4 * drawing_two_from_same_suit

print(f'Total number of possible events for drawing two cards: {drawing_two_from_full_deck}')
print(f'Total number of possible events for selecting two cards of the same suit for the total of 4 suits: {drawing_two_from_same_suit_total}')

P = drawing_two_from_same_suit_total / drawing_two_from_full_deck
print(f'Probability total: {P}')

