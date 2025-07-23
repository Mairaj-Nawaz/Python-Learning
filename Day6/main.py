# # Set

# # set are orderless, unindexed and do not allow duplicates, and cant change
# # a = {1,2,3,4,5}
# # print(a)
# # a.add(6) 
# # print(a)
# # print(type(a))

# # remove an item
# # a.remove(2)
# # print(a)
# # a.remove(2) 

# # discard an item
# # a.discard(3)
# # print(a)

# # a.discard(3)
# # print(a)


# # d = [1, 2, 3, 4, 5, 6]
# # b = set(d)
# # print(b)
# # print(type(b))

# # print(3 in b)
# # print(10 in b)


# # for i in a:
# #     print(i)
    
    
    
 
# # # tuples
# # # tuples are ordered, unchangeable and allow duplicates
# # t = (1, 2, 3, 4, 4, 5)
# # print(t)
# # print(type(t))

# # # Accessing tuple elements
# # print(t[0])  # Output: 1
# # # Iterating through a tuple
# # for item in t:
# #     print(item)

# # # Unpacking tuples
# # a, b, c, d, e ,f = t  
# # print(a, b, c) 
   
# # a = (1,2)
# # b = (3,4)
# # c = a + b   
# # print(c)  

# # a = {1,2}
# # b = {3,4}

# # print(a.union(b))  # Output: {{1, 2}, {3, 4}} - a set of sets

# # print(a | b)  # Output: {{1, 2}, {3, 4}} - another way to union sets


# # Functions

# # def add(a, b):
# #     return a + b

# # def subtract(a, b):
# #     print(a - b)

# # # a = add(5, 10)
# # # print(a)
# # # c = 10 + a
# # # print(c)
# # b = subtract(10, 5)
# # print(b)

# # *Args
# # args datatype is tuple
# def addition(*args):
#     print(type(args))  # Output: <class 'tuple'>
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# a = addition(1, 2, 3, 4, 5)
# print(a)  # Output: 15


# # **kwargs
# # typedict is a dictionary
# def display_info(**kwargs):
#     print(type(kwargs))  # Output: <class 'dict'>
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_info(name="Alice", age=30, city="New York")