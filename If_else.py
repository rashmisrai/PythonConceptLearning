# Python if-else

# 1. IF STATEMENT

'''
a = 23
b = 4

if a <= b:
    print("Hello World")

if a >= b:
    print("The world is sleeping")

if a == b:
    print("A==B")

age = 23
if age >= 18:
    print("Yes, You're eligible", end = " ")
    print("to vote")

democracy = True
if democracy:
    print("Hiii India")

independence = False
if independence:
    print("Hiii all")
else:
    print("Nothing")


a1 = 0  # False
a2 = None  # False
a3 = ""  # False

if a1:
    print("Hii")
else:
    print("Hello")

if a2:
    print("Hello all world")
else:
    print("Hehhe")

if a3:
    print("Jumk")
else:
    print("Pink")

'''

# 2. Elif statement
'''
num1 = 40
num2 = 50

if num1 > num2:
    print("Hello World")
elif num1 > 20 and num2 << 100:
    print("Princess")


# Multiple elif statement

num3 = 80
if num3 ==num1+num2:
    print("Lion")
elif num2 > 50 and num3 < 0:
    print("Tiger")
elif num2 < 100 and num3 < 100:
    print("Rabbit")
elif num1 > 20 and num2 > 20:
    print("Bunny")

'''

# 3. else statement
'''
num1 = 20
num2 = 30
if  num1 > num2:
    print("Cat")
else:
    print("Cow")

# Else as a fallback

username = ""

if len(username) > 0:
    print(f" Hi, {username}")
else:
    print("Error: Empty string")


'''

# 4. shorthand if
'''
a = 23
b = 24

if b > a: print("Happy Birthday")

# shorthand if-else
print("Many happy retuns of the day") if b > a else print("No more birthdays")

# Assign a value with if else

bigger = a if a > b else b
print("Bigger is:", bigger)

biggest = a if a==b else b if a < b else a
print("Biggest is:", biggest)

'''

# 5. Logical operators
'''
age1 = 23
age2 = 34
age3 = 17

if age1 > 18 and age2 > age1:
    print("You can marry")

if age1 > 18 or age2 > age1:
    print("You must marry")

if not age1 < 18:
    print("Marriage")

# combining multiple operators - (use parantheses for the same)
English = 60
Maths = 50
Hindi = 30
History = 50
Science = 80

if (English > Maths and Maths > Hindi) and Hindi > History or History < Science:
    print("Passed")

'''

#6. Nested if
'''
marks = 70
Passed = True

if Passed:
    print("You can apply for the merit list")
    if marks >= 75:
        print("You can take admission in college")
    else:
        print("Try next year")
else:
    print("Retake exam")


'''
#7. Pass statement - acts as a placeholder without doing nothing


age = 35
if age > 50:
    pass  

print("Completed")


def greet():
    pass

print("Function greet")



















