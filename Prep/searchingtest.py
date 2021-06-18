import searching as s

ordered_list = [0,1,2,3,4,5,6,7]

def testSearches():
    assert s.binarySearchI(ordered_list, 9) == -1, "Not found"
    assert s.binarySearchI(ordered_list, 3) == 3, "Found it"
    assert s.binarySearchR(ordered_list, 9) == -1, "Not found"
    assert s.binarySearchR(ordered_list, 3) == 3, "Found it"
if __name__ == "__main__":
    testSearches()
    print("Everything passed")