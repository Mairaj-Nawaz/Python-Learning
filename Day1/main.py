# # Data Types and Basic operations

# # String
# print('This is a string')
# print("This is a string")

# # Integer
# print(10)

# # Float
# print(10.5)

# # Boolean
# print(True)
# print(False)

# # Types 
# name = "Mairaj love javeria"
# print(name)
# print(type(name))

# age = 25 
# print(age)
# print(type(age))

# height = 5.9
# print(height)
# print(type(height))

# available = True
# print(available)
# print(type(available))


# # Type Conversion or casting
# number = "10"
# print(number)
# print(type(number))
# int_number = int(number)
# print(int_number)
# print(type(int_number))
# int_number = float(number)
# print(int_number)
# print(type(int_number))


# Format strings
# name = "Mairaj urf C****Paglu"
# lover= "Javeria"
# print(f"{name} loves {lover}")
# print("{} loves {}".format(name, lover))

# # INPUT
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}, you are {age} years old.")


# Conditions
gender = input("Enter your Gender in (True/False) True means Male and False means Female: ")
print(type(gender))
type_bool = bool(gender)
print(type(type_bool))

if type_bool:
    # Check if the input is a boolean
    # Inintance check data type
    if isinstance(type_bool, bool):
        print("Gender is Male")
    else:
        print("Type Error: Invalid")
else:
    print("No data found")
    