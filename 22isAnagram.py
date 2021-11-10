# Check whether two given strings are an anagram of each other or not.
# An anagram of a string is another string that contains the same characters, only the order of characters can be different.
# For example, “act” and “tac” are an anagram of each other.

class Solution:
    def isAnagram(self,a,b):
        if len(a) == len(b):
            set_a = set(a)
            set_b = set(b)
            #print(set_a, set_b)
            #print(set_a & set_b) - Intersection of both sets
            if (len(set_a & set_b)) == len(set_a) and (len(set_a & set_b)) == len(set_b):
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'

x = Solution()
a = 'b'
b = 'd'
print(x.isAnagram(a,b))