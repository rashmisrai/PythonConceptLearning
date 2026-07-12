# Revising function as of now

#Creating a function
def add(a,b):
    return a+b

print(add(5,6)) # calling a function

# Convert fahereint to celcius

def temp(temp1):
    celsius = (temp1 - 32) * 5 / 9
    return celsius

print(temp(77))

# Parameters and Arguments

def self(name,age):
    print(f"My name is {name} and I'm {age} years old")

self("Rashmi",23)
self("Bunny",24)

# *args and **kwargs

def addition(*numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total

print(addition(3,4,5,6))
print(addition(3,4,5,6,2))


def data(username, **details):
    print(f"Hello {username}, thanks for login")
    print("Additional details: ")
    for key,values in details.items():
        print(key , ":" , values)

data("emil123", age = 25, city = "Oslo", hobby = "coding")


# Python scope
x = 300 # Global variable

def num():
    print(x)

num()


def age():
    x = 200 # local variable
    print(x)

age()
num()

def num1():
    x = 400
    def num2():
        print(x)
    num2()

num1()

def func():
    global x # Global keyword
    x = 500

func()
print(x)

num()


def match():
    score = 0
    def result():
        nonlocal score
        score +=10
        return score

    result()
    result()
    return result()

print(match())


# Python Decorators
'''
user = str(input("Please enter your name: "))
def decorator(func):
    def enjoy(*args):
        print(f"Hi, welcome {user}")
        result = func(*args)
        return result
        print("Thanks for using our website, Have a great time ahead!")
    return enjoy




@decorator
def sum(a,b):
    return a + b

print(sum(10,20))

'''

user = str(input("Please enter your name: "))

def decorator(func):
    def enjoy(*args):
        print(f"Hi, welcome {user}")
        func(*args)
        print("Thanks for using our website, Have a great time ahead!")

    return enjoy

@decorator
def sum(a, b):
    print(a+b)

sum(10,20)

# Lambda in python

x = lambda a,b: a + b
print(x(5,10))
























