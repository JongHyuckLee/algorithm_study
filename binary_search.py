

def binary_search(unsorted_arr, number):
    left, right = 0, len(unsorted_arr)-1

    while True:
        mid = (left+right)/2
        mid_point_value = unsorted_arr[mid]
        if mid_point_value == number:
            return mid
        elif mid_point_value > number:
            right = mid - 1
        elif mid_point_value < number:
            left = mid + 1

    return None

print(binary_search([2, 4, 6, 7, 9, 10, 12, 13], 12))