def get_min_max_array(arr):
    minimum = float('inf')
    maximum = float('-inf')
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]
    return minimum, maximum

print(get_min_max_array([11,2,3,4,5,-6,7,8,9]))
