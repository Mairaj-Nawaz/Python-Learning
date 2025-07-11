# nums = [2, 4, 6, 8, 10]
# ✅ Tasks:

# Count the number of elements in the list without using len().

# Calculate the sum of all numbers using a loop.

# Calculate the average of the numbers.


nums = [2, 4, 6, 8, 10]
sum = 0 
count = 0
avg = 0 

for i in nums:
    count += 1  
    sum = sum + count
    avg = sum / count
print(count)
print(sum)
print(avg)


# for i in nums:
#     count += 1  
# for num in nums:
#     sum = sum + num
#     avg = sum / count
# print(count)
# print(sum)
# print(avg)
