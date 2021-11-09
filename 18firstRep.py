# First repeating character in the string
class Solution:
    def firstRep(self, s):
        for ch in s:
            count = s.count(ch)
            if count > 1:
                return ch
        return '#'

x = Solution()
s = 'geeksforgeeks'
print(x.firstRep(s))
