#John O'Neill 24/03/18 Exercise 4
#2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
#using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

#Need to find Least common Multiple of 11-20!

Numbers = [11,12,13,14,15,16,17,18,19,20]

for i in range(11,21):
    def gcd(a, b):
    #Return greatest common divisor using Euclid's Algorithm."""
     while b:      
        a, b = b, a % b
     return a
    #https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers

for i in range(11,21):
    for a in range(11,b)

        ###no clue!