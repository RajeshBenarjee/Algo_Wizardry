def floor(arr,low,high,x):
    ans=a[0]
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]<=x:
            ans=arr[mid]#if the number is asked to return else return the mid
            low=mid+1
        else:
            high=mid-1
    return ans
a=[1,2,8,10,10,12,19]
print(floor(a,0,len(a)-1,5))
