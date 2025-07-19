# Count Character Frequency
# Given the string:

# python
# Copy
# Edit
# text = "python"
# Create a dictionary that counts the frequency of each character in the string.

text = "python"
count = 0
dict = {
    
}

for char in text:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)


