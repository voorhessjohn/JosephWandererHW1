# The original code is commented out
#import random
#guess = ''
#while guess not in ('heads', 'tails'):
#    print('Guess the coin toss! Enter heads or tails:')
#    guess = input()
#toss = random.randint(0, 1) # 0 is tails, 1 is heads
#if toss == guess:                                      # Bug 1: Always evaluates to False because it checks equivalence of an int with a str. One needs to be converted to the other before comparing the two.
#    print('You got it!')
#else:
#    print('Nope! Guess again!')
#    guesss = input()                                   # Bug 2: A typo in the variable name makes a new, unused variable 'guesss' with an extra 's' instead of reassigning 'guess' with the user's new input.
#    if toss == guess:
#       print('You got it!')
#    else:
#        print('Nope. You are really bad at this game.')

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:                                           # Bugfix 1: Reassigns the 'toss' variable storing the random int with the appropriate string by using conditionals 
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()                                     # Bugfix 2: Fixed the typo so when the user inputs a second guess that guess actually gets checked
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
