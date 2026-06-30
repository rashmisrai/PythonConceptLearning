# Tuples

a = ("Rashmi","Rai",23,23)
print(a)
print(type(a))
print(len(a))


# Creating a tuple with one item requires , after the item
b = ("Apple")
print(b)
print(type(b)) # String

c = ("Mango",)
print(c)
print(type(c)) # Tuple


# Tuple constructor

e = tuple(("Rashmi","Rai",24))
print(e)
print(type(e))

# AccessTuples

f = ("Marigold","Rose","Champa","Periwinkle")
print(f[1])
print(f[-1])


# Range
f = ("Marigold","Rose","Champa","Periwinkle")
print(f[1:3])
print(f[2:])
print(f[:2])
print(f[-3:-1])

if "Rose" in f:
    print("This is a flower")

if "Rose" not in f:
    print("Lion ate it")
else:
    print("Flower is good")


# Change in Tuple
# Note: Tuple is unchangeable but we can convert it into list then again into tuple

g = ("Marigold","Rose","Champa","Periwinkle")
h = list(g)
print(h)
print(type(h))

h.insert(2, "Mogra")
print(h)
g = tuple(h)
print(g)
print(type(g))

# Adding tuple into tuple
i = ("Marigold","Rose","Champa","Periwinkle")
j = ("Mogra",)

j+=i
print(j)

# Remove item from tuple by converting into list

k = ("Marigold","Rose","Champa","Periwinkle","Mogra")
l = list(k)
l.remove("Champa")
k = tuple(l)
print(k)
print(type(k))

# Deleting the tuple completely

m = ("Marigold","Rose","Champa","Periwinkle","Mogra")
del m
# print(m) - This will raise an error because the tuple is empty



# Unpacking tuples

n = ("Marigold","Rose","Champa","Periwinkle","Mogra")
(fruit1, fruit2, fruit3, fruit4, fruit5) = n
print(fruit1)
print(fruit2)
print(fruit3)
print(fruit4)
print(fruit5)


o = ("Marigold","Rose","Champa","Periwinkle","Mogra")
(flower1,flower2,*flower3) = o
print(flower1)
print(flower2)
print(flower3)

p = ("Marigold","Rose","Champa","Periwinkle","Mogra")
(f1,*f2, f3) = p
print(f1)
print(f2)
print(f3)


# Loop in tuple
q = ("Maharashtra", 23.4, "Rashmi", 'A', 9730356673)
print(q)

# 1. For in loop
for x in q:
    print(x)

# loop through index
r = ("Rabbit","bunny","client","Dibu")

for x in range(len(r)):
    print(r[x])

# While loop

s = ("Marigold","Rose","Champa","Periwinkle","Mogra")

loopA = 0
while loopA < len(s):
    print(s[loopA])
    loopA =loopA + 1

# Join tuple
t = ("Marigold","Rose","Champa","Periwinkle","Mogra")
u = ("Rabbit","bunny","client","Dibu")
v = t + u
print(v)

# To get multiple same tuple
w = t *3
print(w)

# Tuple methods
x = ("Marigold","Rose","Champa","Periwinkle","Mogra","Rose")
y = x.count("Rose")
print(y)

z = x.index("Champa")
print(z)
