def insertion_sort(arr,n):

    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            (arr[j-1],arr[j])=(arr[j],arr[j-1])
            j-=1
        
    print(arr)


arr=[12,3,4,1,24,5,2,33,5,21]
insertion_sort(arr[:],len(arr))


# Time Complexity 

# best-O(N)
# average-O(N^2)
# worst-O(N^2)

# Space Complexity
# O(1) auxiliary space. 