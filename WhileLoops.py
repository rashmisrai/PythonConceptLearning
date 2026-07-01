# While loop = as far as the condition is true, loop will execute

num = 0

while num <= 10:
    print("The num is: ", num)
    num += 1

# break in while loop

age = 0

while age <= 18:
    print(age)
    if age == 13:
        break
    age += 1

# continue in while loop

num1 = 0
while num1 < 10:
    num1 += 1
    if num1 == 5:
        continue
    print("nums are: ", num1)

# else in while loop

kg = 0
while kg < 10:
    print(kg)
    kg += 1
else:
    print("kg is not less than equal to 10")

























