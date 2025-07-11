# nested = [[1, 2], [3, 4], [5, 6]]
# ✅ Tasks:

# Print 4 using nested indexing.

# Use a nested loop to print all elements one by one.


x = [[1, 2], [3, 4], [5, 6]]
print(x[1][1])

for i in x:
    for j in i:
        print(j)
print()