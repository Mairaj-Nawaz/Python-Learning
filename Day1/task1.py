"""Make a program that takes age as input string and then 
convert it to integer. If the age is greater than or 
equal to 18, print "You are an adult". If the age is less 
than 18, print "You are a minor". Use type conversion to ensure 
"""

age = int(input("please enter your age : "))
if age >= 18:
    print("you are an adult")
else:
    print("your are a minor")

