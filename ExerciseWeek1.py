# John O'Neill amended 08/04/2108 to add comments
# ...Using coding of Ian McLoughlin.

# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1 #sets initial values for the variables

  while n >= 0:
    i, j = j, i + j #used to step through the Fib iterations
    n = n - 1
  return i #returns the result of the function

# Test the function with the following value.
x = 20
ans = fib(x)
print("Fibonacci number", x, "is", ans)