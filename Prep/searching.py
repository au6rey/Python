# Binary Search
def binarySearchI(array, value):
    lower_bound = int(0)
    upper_bound = int(len(array) - 1)
    while lower_bound <= upper_bound:
        midpoint = int((lower_bound + upper_bound) / 2)
        curr_value = array[midpoint]
        if value == curr_value:
            return midpoint
        elif value < curr_value:
            upper_bound = midpoint - 1
        elif value > curr_value:
            lower_bound = midpoint + 1
    return -1


def binarySearchR(array, value):
    return binarySearch(array, 0, int(len(array) - 1), value)


def binarySearch(array, lower_bound, upper_bound, value):
    if lower_bound <= upper_bound:
        midpoint = int((lower_bound + upper_bound) / 2)
        curr_value = array[midpoint]
        if value == curr_value:
            return midpoint
        elif value < curr_value:
            binarySearch(array, lower_bound, midpoint - 1, value)
        elif value > curr_value:
            binarySearch(array, midpoint + 1, upper_bound, value)
    return -1

