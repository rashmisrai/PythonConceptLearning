# Match in python

food = "Pizza"
match food:
    case "Burger":
        print("Take your burger")
    case "Pasta":
        print("Take your pasta")
    case "Coke":
        print("Take your coke")
    case _:
        print("Not available right now, please order something else")

food2 = "Pizza"
match food2:
    case "Burger":
        print("Take your burger")
    case "Pasta":
        print("Take your pasta")
    case "Coke":
        print("Take your coke")
    case "Pizza":
        print("Take your pizza")
    case _:
        print("Not available right now, please order something else")

day = "Friday"
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Hey, this is a weekday")
    case "Saturday" | "Sunday":
        print("Hey, this is a weekend")


month = 4  
day2 = "Friday"
match day2:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" if month == 5:
        print("Hey, this is a weekday")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" if month == 4:
        print("Hey, this is a new weekday")
    case "Saturday" | "Sunday" if month == 5:
        print("Hey, this is a weekend")
    case "Saturday" | "Sunday" if month == 4:
        print("Hey, this is a weekend")
    case _:
        print("No weekdays or weekends found!")
