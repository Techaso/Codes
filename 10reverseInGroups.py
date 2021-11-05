# Reverse array in groups
# Method: GeeksForGeeks Solution
class Solution:
    def reverseInGroups(self, arr, N, K):
        i=0
        while(i<N): # IMPORTANT: 'for i in range(N)' won't work correctly here, because of shifting of i using i+=K.
            if (i+K<N):
                arr[i:i+K]=reversed(arr[i:i+K])
                i+=K
            else:
                arr[i:]=reversed(arr[i:])
                i+=K
        return arr
arr = [35, 56, 48, 21, 87] #[1,2,3,4,5]
N=5
K=77

x = Solution()
print(x.reverseInGroups(arr,N,K))

'''
METHOD 2:
Problem: This is wrong solution, because we don't need to reverse only 1 subarray but all subarrays of size K, including the last remaining subarray (size < K) after all subarrays of size K
class Solution:	
    def reverseInGroups(self, arr, N, K):
        arr[0:K] = reversed(arr[0:K])
        arr[K:N] = reversed(arr[K:N])
        return arr

METHOD 1:
Problem1: Working fine in laptop but GeeksForGeeks not showing correct output
Problem2: This is wrong solution, because we don't need to reverse only 1 subarray but all subarrays of size K, including the last remaining subarray (size < K) after all subarrays of size K
class Solution:	
    def reverseInGroups(self, arr, N, K):
        Arr1 = arr[0:K]
        Arr2 = arr[K:N]
        Arr1.reverse()
        Arr2.reverse()
        Arr1.extend(Arr2)
        arr = Arr1
        return arr
'''