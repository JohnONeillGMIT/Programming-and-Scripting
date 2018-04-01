
#John O'Neill 01/04/2018
#Euler Problem 5... Finding Lowest common multiple for a range 1-20


def LCM(sum):
    for i in range(11,21):
        if sum % i != 0: # checking if divisible (no remander)
            return False #if divisible, True, if not false
    return True

sum=2520   #already know that 1-10 is covered by 2520
while True:
    if LCM(sum):
        break
    sum+=2520 #idea to step of 2520 taken from here https://www.youtube.com/watch?v=EMTcsNMFS_g
print(sum)


#referenced a number of online solutions.

