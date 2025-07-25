#  Write a function to count vowels in a string
# Requirements:
# Define a function count_vowels(s) that:

# Takes a string s as input.

# Counts the number of vowels (a, e, i, o, u, both upper and lower case).

# Returns the count.


# def count_vowels(s):
#     count = 0
#     for char in s:
#         if char in "a":
#             count += 1
#         elif char == "e":
#             count += 1
#         elif char == "i":
#             count += 1
#         elif char == "o":
#             count += 1
#         elif char == "u":
#             count += 1
#         elif char == "A":
#             count += 1
#         elif char == "E":
#             count += 1
#         elif char == "I":
#             count += 1
#         elif char == "O":
#             count += 1
#         elif char == "U":
#             count += 1
#     print("Vowel count:", count)
# count_vowels("Mairaj nawaz A")



#OR
def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    print("vowel count ", count)
count_vowels("mairaj A")
