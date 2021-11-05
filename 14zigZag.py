# Convert array into Zig-Zag fashion
# HINT: Compare elements and sequence should be < > < > < ...
# HINT: in output, odd indexed element is always greater than its neighbour elements i.e arr[i-1] and arr[i+1]
# IMPORTANT: Method 2 and  this solution is not much different, so memorize the correct solution carefully. Check each element instead of just checking the odd indexed elements (method-2)
class Solution:
    def zigZag(self,arr, n):
        i = 1
        for i in range(n-1):
            if i%2 == 0 and arr[i] > arr[i+1]: # Even indexed numbers
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            elif i%2 == 1 and arr[i] < arr[i+1]: # Odd indexed numbers
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        return arr

x = Solution()
arr = [4, 3, 7, 8, 6, 2, 1]
n = 7
print(x.zigZag(arr,n))

'''
METHOD 2:
Problem: One test case is not passing
class Solution:
    def zigZag(self,arr, n):
        i = 1
        while i < n-1:
            if arr[i] < arr[i-1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
            if arr[i] < arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            i+=2 
        return arr

METHOD 1: Incorrect Solution
class Solution:
    def zigZag(self,arr, n):
        condition = False # False will help to check if arr[i] < arr[i+1] or not
        print(arr)
        for i in range(n-1):
            if condition == False and arr[i] > arr[i+1]:
                j = i
                while arr[i] > arr[i+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                condition = True
                continue
            if condition == True and arr[i] < arr[i+1]: # True will help to check if arr[i] > arr[i+1] or not
                j = i
                while arr[i] < arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                condition = False
                continue
        return arr
'''
