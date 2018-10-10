def selection(list):
    length = len(list)
    lowestIndex = 0
    for i in range(0, length):
        lowestIndex = i
        for j in range(i+1, length):
            if list[j] < list[lowestIndex]:
                lowestIndex = j
        if lowestIndex != i:
            list[i], list[lowestIndex] = list[lowestIndex], list[i]
    return list

unsorted_list = [5, 3, 8, 2, 4]
print(selection(unsorted_list))