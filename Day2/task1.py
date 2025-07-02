# print this pattern
# take length as user input

#            =
#           ==
#          ===
#         ====
#        =====
#       ======
#      =======
#     ========
#    =========
#   ==========
#  ===========
# ============


length = int(input("please enter the length of the pattern: "))
for i in range(length-1):
    for j in range(1, length):
        print("=", end= " ")
    print()
    
   
