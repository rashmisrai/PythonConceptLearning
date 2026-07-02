# Functions in Python
'''
name = str(input())

def username():   # Create a function using def keyword
    print(f" User has entered name as {name}")

username()  # calling the function


# function to change from fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(67))

# pass in function

def learn():
    pass
'''

# 1. Python Arguments
'''
person = str(input("Please enter your email: "))

def data(email): # email => parameter (it is passed wihile creating the function)
    print(f"{email}@gmail.com")

data(person) # person => argument (it is passed while calling the function)
'''
name1 = str(input("Please enter your name: "))
age1 = int(input("Please enter your age: "))

def name(name, age):
    print(f"{name} is {age} years old")

name(name1, age1)

def name2(name = "Rashmi"):
    print(f"{name}")

name2()

# Keyword arguments

def earth(animal, human):
    print(f"Hi, I'm {animal}, and I live with {human}")

earth(human = "Ankit", animal = "Cow")


# Positional arguments

def substract(a,b):
    return a-b

value = substract(5,2)
print(value)

# Keyword and Positional arguments

def my_function(pet,age,name):
    print("My name is", name, "and I'm", age, "years old and have a", pet)

my_function("dog", name = "Rashmi", age = 23)   # First positional argument should be there, then keyword argument is there


    
# Passing different data types

def my_function(fruits):
    for x in fruits:
        print(x)

my_fruits = ["Apple","Mango","Banana"]
myFruits = ("Papaya","Pear","Pomegranate")

my_function(my_fruits)
my_function(myFruits)


state = set(("Maharashtra","Gujrat","MadhyaPradesh"))
my_function(state)


# Returning values in Python using function

def add(c,d):
    return c + d

print(add(2,4))


# Returning values with different data types

def function():
    return ["Sunflower","Sunfeast","Safflower"]

#flower = function()
#print(flower[0])

print(function())


# Returning Different Data Types Based on Conditions
def test(score):
    if score < 50:
        return "Fail"
    elif 70>score>=50:
        return 500
    else:
        return False

print(test(56))


# REAL LIFE EXAMPLE

def cash(withdraw, amount):
    if withdraw <= amount:
        return amount - withdraw
    else:
        return "Insufficient Balance"

print(cash(200, 500))
print(cash(500,200))
print(cash(500,500))

# Positional only arguments
'''
def name(name):
    print("Hello", name)

name("Rashmi")

'''
def name(name, /):
    print("Hello", name)

name("Rashmi")
'''
# This will throw an error because this is strictly positional argument (, /)
def age(age, /):
    print("Age is ", age)

age(age = 23)
'''

# Keyword only arguments

def name(*,name):
    print("Hello", name)

name(name = "Rashmi")


# Combining Positional-Only and Keyword-Only

def student(name, age,/,*, std, div):
    return (f"{name} is {age} years old. She is in class {std} and Div {div}")

s = student("Rashmi",23, std = 9, div = "A")
print(s)



















