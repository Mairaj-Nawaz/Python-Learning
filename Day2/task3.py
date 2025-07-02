# How can you modify the loop to count how many times
# the letter l appears in "Hello, World!"?
text = "hello, world"
count = 0

for i in text:
    if i == "l":
        count +=1
        
print("l in hello world appears ", count, "times")