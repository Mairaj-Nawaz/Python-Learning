# *****
# ****
# ***
# **
# *


count = 0
length = int(input("please enter the length of the pattern: "))
for i in range(length,0,-1):
    count+=1
    for j in range(i): 
        print("=", end="")
    print()