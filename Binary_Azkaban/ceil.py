def flooor(arr,low,high,x):
    ans=arr[0]
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>=x:
            ans=arr[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
a=[1,2,8,10,10,12,19]
print(flooor(a,0,len(a)-1,5))