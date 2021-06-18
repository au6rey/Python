def bubbleSort(array):
    endpoint = len(array) - 1
    sorted = False
    while not sorted: 
        sorted = True
        for curr_index in range(endpoint):
            if (array[curr_index] > array[curr_index + 1]):
                sorted = False
                array[curr_index], array[curr_index +
                                         1] = array[curr_index + 1], array[curr_index]
        endpoint -= 1
    return array
