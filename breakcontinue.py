# break and continue statements

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n // x)
      break
  else:  # the else block will be executed if
        # there is no break happened in the for
        # block. exhaustion of the loop
        #this is the else of the for not the if
    # loop fell through without a factor
    print(n, 'is a prime number')


# test with while loop
i = 10
while i > 0:
  print("i = ", i)
  i -= 1
else:
  print("we quitted while loop")
  print("i = ", i)



##################################
# the continue statement 

for num in range(2,10):
  if num % 2 == 0:
    print("found an even number", num)
    continue
  print("Found a number", num)

########################
# the pass statement 
if True:
  pass # pass is used for empty blocks in Python 
print("we passed successfully")

# an empty Python class 
class MyEmptyClass:
  pass

