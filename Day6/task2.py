# Write a function to return the sum of all even numbers in a list
# Requirements:
# Define a function sum_even_numbers(lst) that:

# Takes a list of integers lst as input.

# Sums only the even numbers.

# Returns the sum.


def sum_even_number(s):
    sum = 0
    a = [2, 5, 3, 9, 23, 54, 78, 87, 99, 4]
    for i in a:
        if i %2 == 0:
           sum += i
    print("total sum is ", sum) 
sum_even_number(None)