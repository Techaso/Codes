# CORRECT WORKING SOLUTION from GeeksForGeeks
class Solution:
    def subArraySum(self,arr, n, s): 
        # Initialize curr_sum as value of first element and starting point as 0
        curr_sum = arr[0]
        left = 0
        right = 1
        # Add elements one by one to curr_sum and 
        # if the curr_sum exceeds the sum, then remove starting element         
        while right <= n:
            # If curr_sum exceeds the sum, then remove the starting elements
            while curr_sum > s and left < right-1:
                curr_sum = curr_sum - arr[left]
                left += 1
            
            # If curr_sum becomes equal to sum, then return true
            if curr_sum == s:
                return [left+1,right]
            # Add this element to curr_sum
            if right <= n-1:
                curr_sum = curr_sum + arr[right]
            right += 1

        # If we reach here, then no subarray
        return [-1]

x = Solution()
arr = [135,101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5,103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
n=42
s=468
print(x.subArraySum(arr,n,s))

'''
01/10/2021
# MY NOT WORKING SOLUTION
class Solution:
    def subArraySum(self, arr, n, s): 
        curr_sum = 0
        left = 0    #  left <=right
        right = 0   # 0 <= right <= n-1, right will work as index number also
        if n >=1 and n <= pow(10,5):
            while right <= n-1:
                #print(" curr_sum = {}, arr[right] = {}, left = {}, right = {}".format(curr_sum,arr[right],left,right))
                if arr[right] < 1 or arr[right] > pow(10,10):
                    #print('here1')
                    return [-1]
                while curr_sum > s and left <= right:
                    #print('here2')
                    curr_sum = curr_sum - arr[left]
                    left += 1
                if curr_sum == s:
                    #print('here3')
                    return [left+1,right] # element_number = index_number + 1
                if right <= n-1:
                    #print('here4')
                    curr_sum = curr_sum + arr[right]
                right += 1 # this needs to increase always, otherwise while loop won't stop

            #print('here last') # outside of while loop
            return [-1]

'''