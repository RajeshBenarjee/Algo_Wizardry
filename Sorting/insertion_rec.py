def insertion_rec(arr,n):
    if n <= 1:
        return arr
    insertion_rec(arr, n - 1)  
    last = arr[n - 1]         
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
    return arr


arr=[12,3,4,1,24,5,2,33,5,21]
print(insertion_rec(arr[:],len(arr)))