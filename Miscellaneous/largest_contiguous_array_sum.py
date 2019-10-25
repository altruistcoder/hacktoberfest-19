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

