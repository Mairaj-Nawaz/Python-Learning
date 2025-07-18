# Dictionary

# dictionary = {
#      "Name" : "John",
#      "Age" : 30,
#      "City" : "New York"
# }
# print(dictionary)


dic = {
    "list": [1, 2, 3, 4, 5],
    "tuple": (1, 2, 3, 4, 5),
    "set": {1, 2, 3, 4, 5},
    "dic" : {"Name": "John"},
    "name": "John",
    1: "one"
}
# print(dic)
# print(dic['list'])

# for key, value in dic.items():
#     print(f"{key}: {value}")


# for value in dic.items():
#     print(f"{key}: {value}")

# # insert
# dic["newkey"] = "mairaj"
# print(dic)
# # delete
# del dic["newkey"]
# print(dic)

# print(dic.keys())
# print(dic.values())

# List of Dictionaries 
list_of_dicts = [
    {
        "Name": "John", 
        "Age": 30, 
        "City": "New York"
    },
    {
        "Name": "John", 
        "Age": 30, 
        "City": "New York"
    }
]

# dictionary with Lists as Values
dict_of_lists = {
    "Name": ["John", "Doe"],
    "Age": [30, 25],
    "City": ["New York", "Los Angeles"]
}
# Enumerate tells us the index and the value
for i in enumerate(list_of_dicts):
    print(i)
    
dict_of_lists["Name"] = ["John", "Doe", "Smith"]
print(dict_of_lists)