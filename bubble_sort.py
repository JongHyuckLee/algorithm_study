def bubble(list):
    index = len(list) - 1 # 정렬되지 않은 데이터까지의 인데스를 나타네기 위한 변수
    is_sorted = False # 정렬 완료 여부 flag

    while not is_sorted:
        is_sorted = True
        for i in range(index):
            if list[i] > list[i+1]:
                is_sorted = False
                list[i+1], list[i] = list[i], list[i+1]
        index = index - 1 # 한 패스스루가 지났을 때 비교가 끝나 제자리를 찾은 값은 더 이상 비교하지 않기 위해 인데스를 하나 줄여줌
    return list

unsorted_list = [4, 2, 7, 1, 3]
print(bubble(unsorted_list))