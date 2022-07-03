"""A coin will be flipped 100 times, I have to know percentage of how many streaks(6) of tails and heads will happen. This will happen 10.000 times"""

from random import randint

head_flip = tails_flip = head_streak = tails_streak = 0
for i in range(10000):
    for j in range(100):
        if randint(0,1) == 0: 
            tails_flip = 0 
            head_flip += 1
            if head_flip == 6: 
                head_streak += 1
                head_flip = 0
        else: 
            head_flip = 0
            tails_flip += 1
            if tails_flip == 6:
                tails_streak += 1
                tails_flip = 0
                
total_streaks = tails_streak + head_streak
print(f'We have {total_streaks/100}% chance of having a streak.')