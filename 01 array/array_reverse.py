def reverse_array(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

a = [1,2,3,4,5,6,7,8,9]
reverse_array(a)
print(a)