# John O'Neill started 09/02/2018 to 13/02/2018.... Exercise Week3
# Applies Collatz conjecture logic https://en.wikipedia.org/wiki/Collatz_conjecture
# Loops until the value comes back as 1



n = int(input("Please enter an Integer: "))


while n !=1:
   if n%2 ==0:
    n= n/2
    n=int(n) #https://stackoverflow.com/questions/3398410/python-get-number-without-decimal-places
    #int makes sure we get a number value as the input to the string...
    print(n) 
   else:
    n= (n*3)+1
    n=int(n)
    print(n)

 # if tests a condition and returns avalue etc...
 # print("some statement") 
 # remaider = 0 (% ==0:
 # elif test another condition...)

