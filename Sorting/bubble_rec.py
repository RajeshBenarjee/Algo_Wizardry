def bubble_rec(arr,n):
    if n==1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            (arr[i],arr[i+1])=(arr[i+1],arr[i])
    return bubble_rec(arr,n-1)

arr=[12,3,4,1,24,5,2,33,5,21]

print(bubble_rec(arr[:],len(arr)))