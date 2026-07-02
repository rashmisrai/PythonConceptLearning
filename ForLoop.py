# Forloop in python
state = ["Maharashtra", "Chattisgarh", "Punjab", "Uttar Pradesh", "Bihar", "Rajasthan", "Gujrat", "Mumbai"]

for x in state:   # Basic for loop
    print(x)

statement ="Rashmi"
word = ("Baby",)

for x in statement:
    print(x)

for x in word:
    print(x)

print(statement[0])
print(word[0])


fruits = {"Banana", "Apple", "Pomegranate", "Pear", "Papaya", "Pumpkin"}

for x in fruits:
    print(x)


for x in fruits:
    print(x)
    if x == "Apple":
        break

for x in state:
    if x == "Bihar":
        continue
    print(x)


for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(2,5,2):
    print(i)

state1 = ["Maharashtra", "Chattisgarh", "Punjab", "Uttar Pradesh", "Bihar", "Rajasthan", "Gujrat", "Mumbai"]

for x in state1:
    print(x)
else:
    print("States list are over")

# Else will not execute if break statement is used
for x in fruits:
    print(x)
    if x == "Apple":
        break
else:
    print("Fruits list are over")


# Nested loop


a = [12,34,567,86]
b = ["Rashmi","Kaya","Ankit","Dubu"]

for x in a:
    for y in b:
        print(f" Roll no: {x}, Name: {y}")


# Pass in loop

for i in range(5):
    pass

















