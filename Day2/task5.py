# =============
#  ============
#   ===========
#    ==========
#     =========
#      ========
#       =======
#        ======
#         =====
#          ====
#           ===
#            ==
#             =


# length = int(input("please enter the length of the pattern: "))
# #count = 0 

# for i in range(length,0,-1):
#     for j in range(length,0,-1): 
#         print("=", end = "")
#     print()


count = 0
length = int(input("please enter the length of the pattern: "))
for i in range(length,-1,-1):
    count+=1
    for j in range(i,-1,-1):
        print(" ", end="")
    for k in range(count):
        print("=", end='')
    print()