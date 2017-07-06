# the for statment 
# ------------------

words = ['cat', 'window', 'defence']

for w in words:
  print (w, len(w))


for w in words[:]:
  if(len(w) > 6):
    words.insert(0,w)
  print(w)

print('after insertion')
for w in words:
  print(w)

# Using range method 

for i in range(0,5):
  print(i,' ', end='')

print(end='\n')

for i in range(0,10,3):
  print(i, ' ', end='')

print(end='\n')

print("i in range(10):")
for i in range(10):
  print(i, ' ', end='')

print(end='\n')

print("""for i in range(len(a)):
   print(i, a[i])""")

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
  print(i, a[i])


# list 
it = list(range(5))
print("it = list(range(5))")
for i in it:
  print(i, ' ', end='')
print(end='\n')

# Continue here : https://docs.python.org/3/tutorial/controlflow.html

