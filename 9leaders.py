# Find leaders in an array
# Leader: An element which is greater than or equal to all the elements on right side
# HINT: Traverse all the elements from right to left in array and check whether the current element is greater than the maximum stored till now.
class Solution:
    def leaders(self, A, N):
        leaders = []
        right_max = A[N-1]
        i = N-1
        while i>=0:
            
            if A[i] >= right_max:
                leaders.append(A[i])
                right_max = A[i]
                
            i-=1
        leaders.reverse() # IMPORTANT: .reverse() doesn't create a new object but modifies the already existing one, so use 'return leaders' instead of 'return leaders.reverse()'. Otherwise it will return None
        return leaders

x = Solution()
A = [16,17,4,3,5,2]
N = 6
print(x.leaders(A,N))


'''
METHOD 1: using max() function to check if current value is maximum
Problem: Time Limit Exceeded
class Solution:
    def leaders(self, A, N):
        leaders = []
        for i in range(N):
            right_max = max(A[i:])
            if right_max == A[i]:
                leaders.append(A[i])
        return leaders
'''