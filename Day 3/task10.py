# *****
#      *****
#           *****
#                *****
# Task:
# Print 4 rows where each ***** starts 5 spaces further than the previous row.

# start count from 0
# isme count check kro total for example:
# fist wala 5 star mtlb 5 count ki value
# 2nd jitne count ki value utni spacing
# 2nd me phr dobara 5 star mtlb 5 more values add to count now count value is 10 
# like this all work


count = 0

n = 10
for i in range(n):
    for j in range(count):
        print("", end=" ")
    for k in range(5):
        print("*", end='')
        count +=1
    print()


