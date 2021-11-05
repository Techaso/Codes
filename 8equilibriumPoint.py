# Find first equilibrium point in the array
# Equilibrium Point: a position such that the sum of elements before it is equal to the sum of elements after it.
class Solution:
    def equilibriumPoint(self,A, N):
        arr_sum = sum(A)
        left_sum = 0

        for i in range(N):
            right_sum = arr_sum - left_sum - A[i]

            if left_sum == right_sum:
                return i+1
            
            left_sum = left_sum + A[i]
        return -1

x = Solution()
A = [1,3,5,2,2]

N = 5
print(x.equilibriumPoint(A,N))
