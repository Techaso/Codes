# Last index of One
# Hint: Start searching from the last index and return the position as soon as it is found
class Solution:
    def lastIndex(self, s):
        n = len(s)
        i = n-1
        while i>=0:
            if s[i] == '1': # IMPORTANT: Put quote around 1, as it is a part of string, not a integer
                return i
            i -= 1
        return -1

x = Solution()
s = '00001'
print(x.lastIndex(s))