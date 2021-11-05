# First element in array with left side smaller elements and right side greater elements
#HINT: Traverse left to right and keep track of maximum element till ith index, similarly traverse right to left and keep track of minimum element till ith index.

def findElement( arr, n):

    #Creating two arrays for storing maximum and minimum values
    left_max = []
    right_min = []

    #Storing random values, to make the array size of n-1
    for i in range(n):
        left_max.append(0) 
        right_min.append(0)
    
    # Initial maximum and minimum values
    max_value = arr[0]
    min_value = arr[n-1]
    
    # filling left_max array with maximum values
    for i in range(n):
        if max_value < arr[i]:
            max_value = arr[i]
        left_max[i] = max_value

    # filling right_min array with minimum values
    for i in range(n):
        if min_value > arr[n-i-1]:
            min_value = arr[n-i-1]
        right_min[n-i-1] = min_value
    
    # Finding first commong element of both arrays, which will satisfy our problem statement
    for i in range(n):
        if right_min[i] == left_max[i] and i != 0 and i != n-1: #IMPORTANT Condition. Memorize it.
            return arr[i]
    
    # If no satisfying element found
    return -1

arr = [4,2,5,7] #[11,9,12]
n = 4

print(findElement(arr,n))

'''
# METHOD 2: Modified form of Method 1, but still incorrect solution
def findElement( arr, n):
    left_max = 0
    right_max = 0
    for i in range(n):
        if n >= 3 and i>0:
            left_max = max(arr[:i])
            right_max = max(arr[i:])
        if arr[i] >= left_max and arr[i] <= right_max:
            return arr[i]
    return -1


METHOD 1: Incorrect solution
Problem: max() arg is an empty sequence
def findElement( arr, n):
    left_max = 0
    right_max = 0
    for i in range(n):
        if n > 3:
            left_max = max(arr[:i])
            right_max = max(arr[i:])
        if arr[i] >= left_max and arr[i] <= right_max:
            return arr[i]
'''
