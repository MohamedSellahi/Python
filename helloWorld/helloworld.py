import string
s = "hello world"
string.capwords(s)
print(s)

# fibonaci series:
# the sum of two numbers defines the next
a, b = 0, 1
while b < 10:
  print(b)
  a, b = b, a + b # all right hand expression is evaluated before  
                  # any assignements  
