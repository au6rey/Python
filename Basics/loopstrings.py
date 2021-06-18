a = "Hello, World!"
print(a[1])

# Looping
# for char in a:
#     print(a.index(char))


def checkString(word):
    if word in a:
        print("Found: " + word)
    if word not in a:
        print("Did not find " + word)
# Length
    print(len(a))


checkString("W")


def sliceWord(word, startIdx, endIdx):
    print("From start: " + word[:endIdx])
    print("To end: " + word[startIdx:])
    print("In the middle: " + word[startIdx:endIdx])
    print("Negative Indexing: " + word[-endIdx:-startIdx])

sliceWord(a, 1,5)

# Format string
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(45, 2, 500))

for i in range(+-):
    print(i)