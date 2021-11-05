# Chocolate Distribution Problem, From GeeksForGeeks
'''
Constraints:
1 ≤ T ≤ 100  T: number of testcases
1 ≤ N ≤ 10^5
1 ≤ A[i] ≤ 10^9
1 ≤ M ≤ N
'''
class Solution():
    def findMinDiff(self, A, N, M):
        if N>=1 and N<=100000 and min(A)>=1 and max(A) <=pow(10,9):
            if M>=1 and M<=N:
                A.sort()

                min_diff = A[N-1] - A[0] # As one subarray is itself A

                for i in range(N-M+1): # n-m is possible number of subarrays
                    min_diff = min(min_diff, A[i +M-1]-A[i]) # Other subarrays of size M, # Example: min(55, arr[4]-arr[0]), min (55, arr[5]-arr[1])
                
                return min_diff
x = Solution()
print(x.findMinDiff([3, 4, 1, 9, 56, 7, 9, 12],8,5))