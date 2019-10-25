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






# Python program for simple calculator 
  
# Function to add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 
  
print("Please select operation -\n" \ 
        "1. Add\n" \ 
        "2. Subtract\n" \ 
        "3. Multiply\n" \ 
        "4. Divide\n") 
  
  
# Take input from the user  
select = input("Select operations form 1, 2, 3, 4 :") 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == '1': 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == '2': 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == '3': 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == '4': 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input") 
