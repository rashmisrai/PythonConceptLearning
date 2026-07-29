# Range in Python
'''
Syntax: range(start, stop, step)

'''
x = range(10)
print(x)
print(type(x))

y = range(5,11)
print(y)
print(list(y))

z = range(3,15,2)
print(z)
print(tuple(z))


# Using range in for loop

for i in range(10):
    print(i+1)

#Slicing in ranges

num = range(10)
print(num[9])
print(num[2:6])
print(list(num[2:6]))
print(num[:5])
print(list(num[:5]))

# Membership Testing 

r = range(2,20,2)
print(6 in r) # True
print(7 in r) # False


# Length

ry = range(2,20,2)
print(list(ry))
print(len(ry))












