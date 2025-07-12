def binary_rec(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_rec(arr,mid+1,high,target)
    # auto else condition
    return binary_rec(arr,low,mid-1,target)


a=[12,34,54,64,66,76,80,86,90]
print(binary_rec(a,0,len(a)-1,80)) 