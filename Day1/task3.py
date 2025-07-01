"""
Make a program with nested if statements that 
will check input types and if input matches the expected type.
Exmaple: 
1-Take input a name and check that if its a string, 
if string is not empty and if its data  type is string.
then proceed if not show error

2- Now take a number as input string convert it to integer
and check if the number is even or odd , and also if the number 
is greater than 10 or not.

if both conditions are met then print the number is even
and greater than 10, else print the number is odd or less than 10.

"""

name = input("please enter your name : ")
print(type(name))

num = int(input("please enter a number: "))


if name:
    if num % 2 and num >= 10:
        print("number is even and greater than 10")
    else:
        print("number is odd and less than 10")
else:
    print("error")