def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [38, 27, 43, 3, 9, 82, 10]
print(linear_search(arr,27))