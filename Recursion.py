# Lambda Revision
a = lambda x: x*x
print(a(3))

def add(a,b,operation):
    return operation(a,b)

print(add(5,6,lambda x,y: x + y))

x  = [("Rashmi",23),("Baby",21)]
xtra = sorted(x, key = lambda a: a[1])
print(xtra)


# Recursion in python

def number(n):
    if n <= 0: # base case
        print("Done")
    else: # Recursive case
        print(n)
        number(n - 1) #Making progress to reach the base case
number(10)

def recursion(n):
    if n == 0:  # base case
        return
    print(n) # Recursive case
    recursion(n-1) #Making progress to reach the base case
recursion(10)

# Note: Without a base case, the function would call itself forever, causing a stack overflow error.

#Factorial of number
def fact(n):
    if n==0 or n==1: # base case
        return 1
    else:
        return n * fact(n-1) # recursive case
    
print(fact(5))

























