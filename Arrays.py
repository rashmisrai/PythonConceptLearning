# Arrays - Python does not have built-in support for Arrays, but Python Lists can be used instead.

food = ["Apple", "Banana", "Chickoo", "DragonFruit", "Eggplant", "Fish"]
print(food)

# Acess array element - through index
print(food[2])
print(food[2:5])

# Add element to an array

#1. append()

food.append("Chicken")
print(food)

#2. insert()
food.insert(1, "Kiwi")
print(food)

#3. extend() - only possible if we want to add 2 arrays
animals =["Cows", "Buffaloes"]
food.extend(animals)
print(food)

# Delete element of an array

#1. remove()
food.remove("Buffaloes")
print(food)

#2. pop()
food.pop(3)
print(food)

#3. del keyword
del food[-2]
print(food)

# Len of an array
print(len(food))


# Looping array element

for i in food:
    print(i)


# Reverse the order of array
food.reverse()
print(food)

# sort()
food.sort(reverse = True)
print(food)
