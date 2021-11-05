# Sort an array of 0s, 1s and 2s
# HINT: we'll shift 0 to left side and 2 to right side, therefore will automatically get shifted in the middle
class Solution:
    def sort012(self,arr,n):
        low = 0
        high = n - 1
        i=0
        while i <= high: # IMPORTANT: i is less than high (a variable), not length of the array
            # We're using i<=high because only middle elements are unsorted, so we don't need to iterate beyond high. After high, either no elements exist or all elements are sorted
            if arr[i] == 0:
                temp = arr[i]
                arr[i] = arr[low]
                arr[low] = temp
                i += 1
                low += 1
            elif arr[i] == 2:
                temp = arr[i]
                arr[i] = arr[high]
                arr[high] = temp
                high -= 1
            else:
                i += 1
        return arr

arr = [0,2,1,2,0]
n = 5

x = Solution()
print(x.sort012(arr,n))