# Dictionaries in Python

student = {
    "name": "Rashmi",
    "age": 23,
    "bloodgroup": "A+",
    "weight in kg": 56
    }
print(student)
print(type(student))
print(student["name"])

student2 = {
    "name": "Rashmi",
    "name": "Bunny",
    "age": 23,
    "bloodgroup": "A+",
    "weight in kg": 56
    }
print(student2) # Duplicates are not allowed

print(len(student2)) # length of dict

details ={
    "name": "Bunny",
    "hobbie": ["Guitar", "Football"]
    }
print(details)

# Access the values

subjects = dict(sub1 = "History", sub2 = "Science", sub3 = "Geography")
print(subjects)

print(details.get("hobbie"))

q = details.keys()
print(q)

s = details.values()
print(s)

details["name"] = "Rashmi"
print(s)

t = details.items()
print(t)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "brand" in thisdict:
    print("Learning dict")
else:
    print("Bye")

if "brand" not in thisdict:
    print("Learning dict")
else:
    print("Bye")


# Update the dict

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict["year"]  = 2002
print(this_dict)

this_dict.update({"brand": "Ferrari"})
print(this_dict)

this_dict["month"] = "July"
print(this_dict)

this_dict.update({"date": 2026})
print(this_dict)

# Removing

this_dict.pop("year")
print(this_dict)

this_dict.popitem()
print(this_dict)

del this_dict["brand"]
print(this_dict)

this_dict.clear()
print(this_dict)

# Loop through dict

students = {
    1: "Rashmi",
    2: "Aman",
    3: "Priya",
    4: "Rohan",
    5: "Neha",
    6: "Arjun",
    7: "Kavya",
    8: "Vikram",
    9: "Sneha",
    10: "Rahul"
}

for x in students:
    print(students[x])

for x in students.keys():
    print(x)

for x in students.values():
    print(x)

for x in students.items():
    print(x)

# Copy in dict

marks = {
    "Math": 95,
    "Science": 88,
    "English": 91,
    "History": 84,
    "Geography": 87,
    "Computer": 99,
    "Physics": 90,
    "Chemistry": 85,
    "Biology": 89,
    "Hindi": 93
}

marks_copy = marks.copy()  #Copy()
print(marks_copy)

marks2 = dict(marks) # Dict()
print(marks2)


# Nested dictionaries

myFamily = {
    "child1" : {
        "name": "Rashmi",
        "age": 23
        },
    "child2": {
        "name": "Bunny",
        "age": 24
        }
    }
print(myFamily)

# OR

Child1 = {
     "name": "Rashmi",
        "age": 23
        }
Child2 = {
    "name": "Bunny",
        "age": 24
        }
myFamilyy = {
    "child1": Child1,
    "child2": Child2
    }
print(myFamilyy)
    
print(myFamily["child1"]["name"])


# Loop through nested dict in python

students = {
    101: {
        "name": "Rashmi",
        "age": 22,
        "course": "MCA"
    },
    102: {
        "name": "Aman",
        "age": 21,
        "course": "BCA"
    },
    103: {
        "name": "Priya",
        "age": 23,
        "course": "MBA"
    }
}

for roll_no,details in students.items():
    print("Roll no:", roll_no)
   # print("Details:", details)

    for key, value in details.items():
        print(key, ":", value)

    print()














