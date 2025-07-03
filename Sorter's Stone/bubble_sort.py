def bubbble_Sort(arr,n):
    for i in range(n):
        swapped=0
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
                swapped=1
        if swapped==0:
            break
    print(arr)



arr=[12,3,4,1,24,5,2,33,5,21]

bubbble_Sort(arr[:],len(arr))

# Time Complexity


# Best Case: O(n) 
# AverageCase : O(N^2) 
# Worst Case: O(N^2) 


# Space Complexity 
# O(1) as it only uses a constant amount of space for the variables.