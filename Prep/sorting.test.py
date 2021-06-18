import sorting as s
unordered_list = [4, 9, 0, 1, -26, -5, -89]

def testSort():
    # assert s.bubbleSort(unordered_list) == [ -26, 0, 1, 4, 9], "Bubble Failed"
    print(s.bubbleSort(unordered_list))

if __name__ == "__main__":
    testSort()
    print("Everything passed")