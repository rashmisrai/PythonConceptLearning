# Sets in python
'''
set_a = {"apple","banana","mango"}
print(set_a)
print(type(set_a))

# Duplicates are not allowed, will be ignored
set_b = {"apple","banana","mango", "apple"}
print(set_b)

set_c = {1, True, 0, False} # True and 1 are considered as same, so anyone of them will be ignored, and same for 0 and False
print(set_c)


print(len(set_b))

# Set can contain different data type

set_d = {"Lion",12, 23.45, True}
print(set_d)

# Can create set using set() constructor
set_e = set({"Rashmi",23,"Rai"})
print(set_e)
print(type(set_e))

# cannot access items through index as it is 'unordered' but can be accessed by for loop

set_f = {"Apple","Mango","Banana","Pear","Papaya","Orange"}
for x in set_f:
    print(x)

print("Pear" in set_f)
print("Pomegranate" in set_f)

print("Pear" not in set_f)
print("Pomegranate" not in set_f)



# Add set item
set_g = {"Apple","Mango","Banana","Pear","Papaya","Orange"}
set_g.add("Kiwi")
print(set_g)

set_h = {"Haridwar", "Kailash"}
set_h.update(set_g)
print(set_h)

set_i = {"Apple","Mango","Banana","Pear","Papaya","Orange"}
myList = ["Rashmi","Rai"]
set_i.update(myList)
print(set_i)

# Remove set item
set_j = {"Apple","Mango","Banana","Pear","Papaya","Orange"}
set_j.remove("Pear")
print(set_j)

set_j.discard("Mango")
print(set_j)

set_j.pop()
print(set_j)

set_j.clear()
print(set_j)

del set_j
# print(set_j) - This will throwa an error because the set is already delete


# Loop set
set_k = {"Cat", "Dog", "Rabbit", "Horse"}

for x in set_k:
    print(x)


# Join set

set1 = {"Math", "Science", "English", "History"}
set2 = {"Science", "Geography", "Math", "Computer"}
set3 = set1.union(set2) # union method returns a new set
print(set3)


set4 = set1 | set2
print(set4) #You can use the | operator instead of the union() method, and you will get the same result.

classA = {101, 102, 103, 104, 105}
classB = {104, 105, 106, 107, 108}

set5 = set1.union(set2,classA,classB) # We can join multiple sets
print(set5)

set6 = set1 | set2 | classA | classB
print(set6)

list1 = ["Apple", "Mango"]
tuple1 = ("Banana", "Orange")

set7 = set1.union(list1, tuple1)
print(set7)
'''
'''
set8 = set1 | list1 | tuple1 # | operator allows you to join only sets, not other data types
print(set8)


set1.update(classA) # The update() method inserts all items from one set into another.
print(set1)


set8 = set1.intersection(set2)  # The intersection() method will return a new set, that only contains the items that are present in both sets.
print(set8)

set9 = set1 & set2 #You can use the & operator instead of the intersection() method, and you will get the same result.
print(set9)


Data1 = {"Math", "Science", "English", "History"}
Data2 = {"Science", "Geography", "Math", "Computer"}
Data1.intersection_update(Data2) # The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
print(Data1)

new = classA.difference(classB)  # The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
print(new)

new1 = classA - classB #You can use the - operator instead of the difference() method, and you will get the same result.
print(new1)

classA.difference_update(classB) # Use the difference_update() method to keep only the items from the first set that are not present in the other set:
print(classA)


A = {"Math", "Science", "English", "History"}
B = {"Science", "Geography", "Math", "Computer"}

C = A.symmetric_difference(B) # The symmetric_difference() method will keep only the elements that are NOT present in both sets.
print(C)

D = A ^ B # You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
print(D)

A.symmetric_difference_update(B) # The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
print(A)

# Frozenset in python

students = frozenset({"Rashmi","Bunny","Ankit","Baby", "Nia"," Kiara"})
print(students)
print(type(students))

newStudents = students.copy() # Creates a shallow copy and refer to the same object
print(newStudents)

print(newStudents is students)

state = frozenset({"Maharashtra", "Telengana", "Kashmir", "U.P"})
state2 = frozenset({"Jharkhand", "Maharashtra", "U.P","Punjab"})

state3 = state - state2 # Returns a new frozenset with the difference
print(state3)

state4 = state & state2
print(state4) # Returns a new frozenset with the intersection

print(state.isdisjoint(state2)) # Returns True if there is NO intersection between two frozensets

p = frozenset({})
d = frozenset({})
print(p.issubset(d)) # Returns True if this frozenset is a (proper) subset of another

print(p <= d) # The <= operator also checks for a subset

rest = frozenset({12,23,345,677})
test = frozenset({12,23})

print(rest.issuperset(test)) # Returns True if this frozenset is a (proper) superset of another

print(rest >= test) # The >= operator also checks for a superset


feel = rest.union(test)
print(feel)

seel = rest  | test
print(seel)


'''


# Set methods


classA = {"Rashmi","Bunny","Ankit","Baby","Dibu","Tungi"}
print(classA)

classA.add("Dibiya")
print(classA)

classA.clear()
print(classA)


Animals = {"Cat", "Dog", "Rabbit", "Horse"}
classAnimals = Animals.copy()
print(classAnimals)
print(classAnimals == Animals)

A = {"Math", "Science", "English", "History"}
B = {"Science", "Geography", "Math", "Computer"}

C = A.difference(B)
print(C)

A.difference_update(B)
print(A)

classB = {"Rashmi","Bunny","Ankit","Baby","Dibu","Tungi"}

classB.discard("Tungi")
print(classB)

AA = {"Math", "Science", "English", "History"}
BB = {"Science", "Geography", "Math", "Computer"}
CC = AA.intersection(BB)
print(CC)

AA.intersection_update(BB)
print(AA)


Animals1 = {"Cat", "Dog", "Rabbit", "Horse"}
Animals2 = {"Bear", "Tiger","Lion"}

print(Animals1.isdisjoint(Animals2))
print(Animals1.issubset(Animals2))
print(Animals1.issuperset(Animals2))

Animals1.pop()
print(Animals1)

Animals2.remove("Lion")
print(Animals2)

AAA = {"Math", "Science", "English", "History"}
BBB = {"Science", "Geography", "Math", "Computer"}

CCC = AAA.symmetric_difference(BBB)
print(CCC)

AAA.symmetric_difference_update(BBB)
print(AAA)

Animals3 = {"Cat", "Dog", "Rabbit", "Horse"}
Animals4 = {"Bear", "Tiger","Lion"}
h = Animals3.union(Animals4)
print(h)

Animals3.update(Animals4)
print(Animals3)
