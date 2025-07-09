# Lists

# x = [1,"string", 2.2, [1,2,3,4],{"name":"mairaj"},(1,2,3)]
# print(x[2])
# print(x[3][2])
# print(x[1][3])
# print(x[4]["name"])

# print(x[2:5])
# print(x[-2])
# print(x[-1])

# for i in x:
#     print(i)
    
# for i in range(len(x)):
#     print(x[i])

x = [1,"string", 2.2, [1,2,3,4],{"name":"mairaj"},(1,2,3)]
# count = 0
# for i in range(len(x)):
#     # print(i)
#     count +=1
# print(count)    


x.append(1)
x.insert(1,"avv")
print(x)
x[0] = 2
x.pop(5)
x.remove([1, 2, 3, 4])
print(x)