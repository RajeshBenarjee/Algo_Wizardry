def binary_itr(arr,low,high,target):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1

a=[12,34,54,64,66,76,80,86,90]
print(binary_itr(a,0,len(a)-1,80)) 