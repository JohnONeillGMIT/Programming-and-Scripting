
#John O'Neill 01/04/2018
#Euler Problem 5... Finding Lowest common multiple for a range 1-20
#'''Used much of logic from https://www.youtube.com/watch?v=Km36RkQToqo and adjusted some variable inputs based on other knowledge on LCM from other sources'''
# https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers


def LCM(sum):
    for i in range(11,21):#goes through the range 11-20
        if sum % i != 0: # checking if divisible (no remainder)
            return False #if divisible, True, if not false
    return True

sum=2520   #already know that 1-10 is covered by 2520
while True: #where divisible
    if LCM(sum):
        break
    sum+=2520 #idea to step of 2520 taken from here https://www.youtube.com/watch?v=EMTcsNMFS_g
print(sum)


# challanging one!! referenced multiple of online solutions.

