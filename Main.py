import SearchAlgorithms as sa

'''
INPUT_FILE_PATH = './listToSort.txt'

file = open(INPUT_FILE_PATH, 'r')

input_text = file.read()
str_array = input_text.split()
array = []

for string in str_array:
    array += [int(string)]

print(len(array))

print(sa.merge_sort(array)[:10])

'''

print(sa.radix_sort([0, 1, 2, 1, 0, 11]))