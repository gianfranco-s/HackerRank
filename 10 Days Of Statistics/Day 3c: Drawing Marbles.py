'''
A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement.
If the first marble drawn is red, what is the probability that the second marble is blue?
'''

# We only need to compute the probability of the second event, that is to say, the probability that the second marble is blue: P_blue

# After one red marble is drawn, we're left with 2 reds and 4 blues, so the sample space would be
S = ('r', 'r', 'b', 'b', 'b', 'b')

# In this case then,
P_blue = S.count('b')/len(S)

print(f'Probability of finding a blue marble: {P_blue}')

