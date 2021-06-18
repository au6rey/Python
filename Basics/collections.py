# # List
# numbers = [1, 2, 3, 4, 5, 6, ]


# # Unpacking
# x, y, z, g, h, i = numbers
# print("Unpacked numbers: ", x, y, z, g, h, i)

# # Tuple
# tupl = ("Name", 50, 0.0023)
# index = tupl.index(50)

# #You can change Lists but not tuples
# numbers.append(90)
# print("New numbers: ", numbers)
# print(index)

# Set
strSet = {"ab", "A", "ab"}
strSet.add("asd")

print(strSet, len(strSet))
# Frozen Set is immutable
froze = frozenset(strSet)
print(froze)

# Dictionary
dictionary = {
    "name": "John",
    "age": 36,
    "scores": {
        "Math": 100,
        "CSC": "A"
    }}

print(dictionary["scores"])
