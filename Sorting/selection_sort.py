def selection_sort(arr,n):
    # find the min in arr every time and set is place 
    for i in range(n):
        # find the min index 
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        # swap min index with i 
        (arr[min_index],arr[i])=(arr[i],arr[min_index]) # if wanted swap only if i!=j for removing un nessary swap operations

    print(arr)

arr=[12,3,4,1,24,5,2,33,5,21]

selection_sort(arr[:],len(arr))


# Time Complexity
# best - O(N^2)
# average - O(N^2)
# worst - O(N^2)  

# Space Complexity
# O(1)  because we are not using any extra space.