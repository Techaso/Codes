# Count the triplets
# HINT: sort the array first. then the problem reduces to find the triplet where two numbers giving sum X.
# Brute force solution will have O(n^3) time complexity. we'll have to use three loops to make all possible pairs after sorting, to check condition
# We want solution with O(n^2) time complexity


'''
METHOD 1: Incorrect Solution, Sorting array and checking three continuous values
Problem: All pairs are checked through this method so it won't give correct answer in all cases
'''
class Solution:
    def countTriplet(self, arr, n):
        arr.sort()
        print(arr)
        count = 0
        i = 0
        while i < n-2:
            j=i+2
            while j<n:
                print(i,i+1,j,'arry values->', arr[i],arr[i+1],arr[j])
                if arr[i] + arr[i+1] == arr[j]:
                    print('here')
                    count += 1
                    break
                j +=1
            i+=1
        return count

x = Solution()
arr = [12, 8, 2, 11, 5, 14, 10] #[1,5,3,2]
n = 7
print(x.countTriplet(arr,n))
