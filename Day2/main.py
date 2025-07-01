# # Match case with loops

# # Calculator

# num1 = int(input("Enter Value1 : "))
# num2 = int(input("Enter Value2 : "))
# option = input("Enter operation (+, -, *, /, //, %, **): ")

# # match case

# match option:
#     case "+":
#         result = num1 + num2
#         print(f"Addition Result: {result}")
#     case "-":
#         result = num1 - num2
#         print(f"Subtraction Result: {result}")
#     case "*":
#         result = num1 * num2
#         print(f"Multiplication Result: {result}")
#     case "/":
#         result = num1 / num2
#         print(f"Division Result: {result}")
#     case "//":
#         result = num1 // num2
#         print(f"Floor Division Result: {result}")
#     case "%":
#         result = num1 % num2
#         print(f"Modulus Result: {result}")
#     case "**":
#         result = num1 ** num2
#         print(f"Exponentiation Result: {result}")
#     case _:
#         print("Invalid operation")


# Loops:

# n = 5
# # Looping through a range of numbers (n-1)
# for i in range(1, n+1):
#     print(f"Current number: {i}")


# n = 5
# for i in range(n):
#     print(f"Current number: {i}")

# n = 8
# for i in range(0, n, 2):
#     print(f"Current even number: {i}")

# Reverse loop example:
# n = 5
# for i in range(n, 0, -1):
#     print(f"Current number: {i}")


# string = "Hello, World!"
# for i in string:
#     print(f"Current character: {i}")



# While loop example:
# count = 0
# while count <= 5:
#     print(f"Current count: {count}")
#     count += 1
#     print(f"Count is: {count}")


# Fabonacci series example:
# n = int(input("Enter the number of terms in the Fibonacci series: ")) 
# a = 0 # starting number
# b = 1 # next number in the series or gap between numbers

# 0, 1, 1, 2, 3, 5, 8, 13, 21
# for i in range(n):
#     print(a, end = ",")
#     c = a + b  # 0+1, 1+1, 1+ 2,
#     a = b   # 1, 1, 2
#     b = c   #1, 2, 3


# *
# **
# ***
# ****
# *****


# Nested Loop

pattern = int(input("Enter design Length: ")) 
# 10
for i in range(pattern): # 0, 1, 2, 3
    for j in range(0, i+1): # 0+1, 1+1, 2+1, 3+1
        print(i, end = "")
    print()
    
