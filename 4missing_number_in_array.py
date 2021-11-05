# Missing number in array

# Method - 2: use sum formula for first first n natural numbers i.e. sum = n(n+1)/2
# constrains: 1 ≤ N ≤ 10^6, 1 ≤ A[i] ≤ 10^6 where A is array. we're using min and max concept for the second constraint, because we don't have a loop where we can check each value of the array
class Solution:
    def MissingNumber(self,array,n):
        if ( n >= 1 and n <= 1000000 ) and ( min(array) >= 1 and max(array) <= 1000000 ): # Constraints
            return int(n*(n+1)/2) - sum(array)

"""
# Method - 1: check the repetition count
# Time Limit Exceeded
class Solution:
    def MissingNumber(self,array,n):
        if n >=1 and n <= pow(10,6):
            for i in range(1,n+1):
                if array.count(i) == 0: # i is not found in array, means it's the missing element
                    return i
                elif array.count(i) == 1: # Checking if i exists in array, if yes then check if it fulfill the constraint
                    if i < 1 or i > pow(10,6):
                        return
                else:
                    pass

"""