# Take two lists in a function and convert them into a tuple separtely
# Then merge both tuples and return the merged tuple
# Requirements:
# Define a function merge_tuples(list1, list2) that:
# Takes two lists list1 and list2 as input.
# Converts both lists into tuples.
# Merges both tuples.
# Returns the merged tuple.


def merge_tuples(a, b):
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9]
    tup = tuple(a)
    tup1 = tuple(b)
    c = tup + tup1
    return c
    
print(merge_tuples(None, None))
