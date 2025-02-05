def selection_sort(array, asc = True):
    return_array = []
    working_array = [item for item in array]

    for i in range(len(working_array)):
        temp_index = None
        for j in range(len(working_array)):
            if temp_index == None or \
                (asc and working_array[j] < working_array[temp_index]) or \
                (not asc and working_array[j] > working_array[temp_index]):
                temp_index = j
        return_array += [int(working_array.pop(temp_index))]
    
    return return_array

def insersion_sort(array, asc = True):
    return_array = [array[0]]

    for i in range(1, len(array)):
        for j in range(len(return_array)):
            if (asc and array[i] < return_array[j]) or (not asc and array[i] > return_array[j]):
                return_array = return_array[:j] + [array[i]] + return_array[j:]
                break
            if j == len(return_array) - 1:
                return_array += [array[i]]
    
    return return_array

def quick_sort(array, asc = True):
    if len(array) < 2:
        return array

    return_array = []
    working_array = [item for item in array]

    pivot = working_array[len(working_array) - 1]
    left_array = []
    right_array = []

    for i in range(len(working_array) - 1):
        if (working_array[i] < pivot and asc) or (working_array[i] > pivot and not asc):
            left_array += [working_array[i]]
        else:
            right_array += [working_array[i]]

    return quick_sort(left_array, asc) + [pivot] + quick_sort(right_array, asc)


def merge_sort(array, asc = True):
    return_array = []

    # Base case
    if len(array) < 2:
        return array
    
    # Otherwise, recurse!
    left_half = merge_sort(array[len(array) // 2:], asc)
    right_half = merge_sort(array[:len(array) // 2], asc)

    # A bit cheeky
    while True:
        if len(left_half) < 1:
            return return_array + right_half
        if len(right_half) < 1:
            return return_array + left_half
        # If the "left element" needs to go first and go to the next comparison
        if (asc and left_half[0] < right_half[0]) or (not asc and left_half[0] > right_half[0]):
            return_array += [left_half.pop(0)]
            continue
        # Otherwise add the "right element" and go to the next comparison
        return_array += [right_half.pop(0)]
    
    return return_array

def HeapSort(array, asc = True):
    pass

def RadixSort(array, asc = True):
    pass

def ShellSort(array, asc = True):
    pass

def BubbleSort(array, asc = True):
    sorted = False
    return_array = array

    # Loop over array until it's "sorted"
    while not sorted:
        # Declare a variable to see if a swap is done during this iteration
        no_swaps = True

        for i in range(len(return_array) - 1):
            # Checks to see if items need swapping, both for ascending and descending sorts
            if (asc and return_array[i] > return_array[i + 1]) or (not asc and return_array[i] < return_array[i + 1]):
                    temp_value = return_array[i]
                    return_array[i] = return_array[i + 1]
                    return_array[i + 1] = temp_value

                    # Set this variable to show that a swap was done and another iteration should be made
                    no_swaps = False
        # Considered sorted if no swaps occurred during an iteration
        sorted = no_swaps
    
    return return_array

def CockTailShakerSort(array, asc = True):
    pass

def GnomeSort(array, asc = True):
    pass

def BitonicSort(array, asc = True):
    pass

def BogoSort(array, asc = True):
    pass

def TimSort(array, asc = True):
    pass

def CombSort(array, asc = True):
    pass

def ExchangeSort(array, asc = True):
    pass

def CountingSort(array, asc = True):
    pass

def BucketSort(array, asc = True):
    pass
