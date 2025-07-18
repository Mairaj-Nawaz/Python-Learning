#Number Classification

# num = [1,2,3,4,5,6,7]                     

# for i in num:
#     if i % 2== 0:
#         print("it is an even number")
#     else:
#         print("it is an odd number")
# print()




#Multiplication Table

# table = int(input("please enter a number to print it's table: "))

# for i in range(11):
#     print(f"{table} * {i} = {table * i}")




#Character Type counter

# text = input("please enter a text: ")

# letters = 0
# digits = 0
# symbols = 0

# for character in text:
#     if character.isalpha():
#         letters += 1
#     elif character.isdigit():
#         digits += 1
#     else:
#         symbols += 1
# print(f"letters = {letters}, digits = {digits}, symbols = {symbols}")




#Grade Assigner for multiple students

# marks = [20, 90, 95, 45, 67, 86, 65, 73]

# for i in marks:
#     if i >= 87:
#         print("congrats you got A grade")
#     elif i >= 78:
#         print("you got B+ grade")
#     elif i >= 72:
#         print("you got B grade")
#     elif i >= 67:
#         print("you got C+ grade")
#     elif i >= 60:
#         print("you got C grade")
#     else:
#         print("you failed the course")
#     print()




# Sum of n numbers

# num = int(input("please enter N numbers: "))
# total = 0

# for i in range(1, num+1):
#     total += i
# print("total sum is = ", total)




# Finding largest number in the list

# nums = [10, 43, 1, 35, 87, 90]
# largest = nums[0]

# for num in nums:
#     if num >= largest:
#         largest = num
# print("this is the largets number in the list : ", largest)




#Multiple of 3

# start = int(input("please enter the starting number: "))
# end = int(input("please enter the ending number: "))
# count = 0

# for i in range(start, end + 1):
#     if i %3 == 0:
#         count += 1
# print("multiples of 3 ", count)




# Check if a word is Palindrome or not

# word = input("please enter a word: ")
# rev_word = ""

# for char in word:
#     rev_word = char + rev_word
# if rev_word == word:
#     print("the word is a palindrome")
# else:
#     print("the word is not a palindrome")




# Hotel Menu Project

#Dictionary
# menu = {
#     "daal": 100,
#     "handi": 500,
#     "karahi": 400,
#     "chae": 70,
#     "chapati": 20
# }
# total = 0
# print("Welcome to the restaurent, this is our menu: \n", menu)

# item = input("what would you like to order? ")

# if item in menu:
#     total += menu[item]
#     print(f"your item {item} has been added to your order: ")
# else:
#     print("please order something that is in the menu")
    
# another_item = input("would you like to order anything else? (yes/no) ")

# if another_item == "yes":
#     item_2 = input("please enter the name of the second item: ")
    
#     if item_2 in menu:
#         total += menu[item_2]
#         print(f"your item {item_2} has been added to your order: ")
#     else:
#         print("please order something that is in the menu")
# print(f"the total amount of the ordered items is: ", total)




