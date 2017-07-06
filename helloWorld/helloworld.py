import string
s = "hello world"
string.capwords(s)
print(s)

# fibonaci series:
# the sum of two numbers defines the next
a, b = 0, 1
while b < 10:
    print(b, end=''),
    a, b = b, a + b   # all right hand expression is evaluated before
    # any assignements
print(end='\n')
print("the final value of a and b are: ", a, b)

#####################################

# get input from user
x = int(input("Please enter an integer: "))
if x < 0:
  x = 0
  print('Negative changed to zero')
elif x == 0:
  print('Zero')
elif x == 1:
  print('Single')
else:
  print('More')

