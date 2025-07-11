# z = [1, 2, 3, 4, 5]
# ✅ Tasks:

# Replace the 3 with 99.

# Append 6 to the end.

# Insert 0 at the start.

# Remove 4 from the list.

# Pop the last element and print it.

x = [1, 2, 3, 4, 5]
print(x)

x[2] = 99
print(x)

x.append(6)
print(x)

x.insert(0,0)
print(x)

x.remove(4)
print(x)

y = x.pop()
print(x)
print(y)