# Sum All Values that are Integers in a Dictionary

sum = 0
dict = {
    "a" : 5,
    "b" : 45,
    "c" : "mairaj",
    "d" : 2.5,
    "e" : 50
}

for values in dict.values():
    if isinstance(values, int):
        sum += values
print(sum)