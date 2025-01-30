from random import randrange

array = []

big_number = 10000
while len(array) < big_number:
    temp = randrange(big_number)
    if temp not in array:
        array += [temp]

print(array[10:20])

file = open('listToSort.txt', 'w+')

for i in range(len(array)):
    if i == len(array) - 1:
        file.write(str(array[i]))
        break
    file.write(str(array[i]) + ' ')