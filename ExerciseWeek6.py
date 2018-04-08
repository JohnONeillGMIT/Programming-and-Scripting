#John O'Neill 08/04/2016
#Creating a Function to retuen a Factorial of an Integer (eg 5*4*3*2*1)
#Create Variables,get the input,loop in the function , make it generic!


def Factorial(n): #Function takes an input to the function
  Sum=1
  for i in range(1,n+1):
    Sum *= i # *= adds number to itself (sum= sum*i)
  return Sum #return keyword gives the output of a function

n = int(input("Please enter an Integer: "))

print("The Result for Factorial:" Factorial(n))


