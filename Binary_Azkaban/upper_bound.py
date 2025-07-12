def lower_bound(arr,low,high,target):
    ans=high+1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans


a=[12,34,54,64,66,76,80,86,90]
print(lower_bound(a,0,len(a)-1,86))