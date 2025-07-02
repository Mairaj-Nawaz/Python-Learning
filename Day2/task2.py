# Write a Python program using match-case that takes an integer input (1-4) and prints:

# If the user enters 1 → print "You chose Apple"

# If the user enters 2 → print "You chose Banana"

# If the user enters 3 → print "You chose Orange"

# If the user enters 4 → print "You chose Mango"

# For any other number, print "Invalid choice"

num = input("please enter a number from (1,2,3,4): ")

match num:
    case "1":
        print("you chose apple")
    case "2":
        print("you chose banana") 
    case "3":
        print("you chose orange") 
    case "4":
        print("you chose mango")
    case _:
        print("invalid choice")      