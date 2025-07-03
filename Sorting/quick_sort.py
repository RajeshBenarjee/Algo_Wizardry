def partition(arr, low, high):
    pivot = arr[low]  # pivot value
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

arr = [12, 3, 4, 1, 24, 5, 2, 33, 5, 21]
sorted_arr = quicksort(arr[:], 0, len(arr) - 1)
print(sorted_arr)
