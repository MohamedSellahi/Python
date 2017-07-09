# working with functions
#########################

# function that prints fibonaci series to an arbitraty boundary 
def fib(n):
  """ Print a Fibonaci series up to n """
  a, b = 0, 1
  while a < n:
    print(a, ' ', end=' '),
    a, b = b, a+b

# fib function with return statement 
def fib2(n):
  """ returning the fib series as a list """
  a, b = 0,1
  result = []
  while a < n:
    result.append(a)
    a, b = b, a+b
  return result


# Now call the function 
fib(200)
l = fib2(200)

# continue here 
# https://docs.python.org/2/tutorial/controlflow.html
# 4.7. More on Defining Functions

