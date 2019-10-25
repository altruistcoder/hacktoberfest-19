from sys import maxsize

# Function to find the contiguous subarray whose sum is maximum in the array and also print this subarray
def maxSumSubarray(a, n):
    max_total = -maxsize - 1
    max_curr = 0
    start = 0
    end = 0
    s = 0
    for i in range(0, n):
        max_curr += a[i]
        if max_total < max_curr:
            max_total = max_curr
            start = s
            end = i
        if max_curr < 0:
            max_curr = 0
            s = i + 1
    print("Maximum Contiguous Sum in given array:", max_total)
    print("Maximum Sum Subarray: ", a[start:end+1])

a = list(map(int, input("Enter the array: ").split()))
maxSumSubarray(a, len(a))

# Python program for reversal algorithm of array rotation 
  
# Function to reverse arr[] from index start to end 
def rverseArray(arr, start, end): 
    while (start < end): 
        temp = arr[start] 
        arr[start] = arr[end] 
        arr[end] = temp 
        start += 1
        end = end-1
  
# Function to left rotate arr[] of size n by d 
def leftRotate(arr, d): 
    n = len(arr) 
    rverseArray(arr, 0, d-1) 
    rverseArray(arr, d, n-1) 
    rverseArray(arr, 0, n-1) 
  
# Function to print an array 
def printArray(arr): 
    for i in range(0, len(arr)): 
        print arr[i], 
  
# Driver function to test above functions 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2) # Rotate array by 2 
printArray(arr) 
