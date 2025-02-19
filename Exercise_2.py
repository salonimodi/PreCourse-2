# Python program for implementation of Quicksort Sort 
# give you explanation for the approach
# time complexity: O(logn) 
# Space complexity: O(logn) 
def partition(arr,low,high):
    i = low
    j = high - 1
    pivot = arr[high]
    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if high > low:
        partition_pos = partition(arr, low, high)
        quickSort(arr, low, partition_pos-1)
        quickSort(arr, partition_pos+1, high)      

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
