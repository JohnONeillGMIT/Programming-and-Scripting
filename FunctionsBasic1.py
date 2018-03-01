#John O'Neill 01/03/2018 trying to figure out Functions
# taken from https://www.learnpython.org/en/Functions and playing around

def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()
my_function_with_args("John","you legend")
x=sum_two_numbers(5, 9)
print(x)

#getting there! NB x = function, and tell to return the sum