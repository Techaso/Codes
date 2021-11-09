# Remove common characters and concatenate uncommon characters of strings s1 and s2
# Method-2
class Solution:
    def concatenatedString(self,s1,s2):
        # String to set conversion
        set1 = set(s1)
        set2 = set(s2)
        common_chars = list(set1 & set2) # Intersection of two sets
        s1 = [ch for ch in s1 if ch not in common_chars]
        s2 = [ch for ch in s2 if ch not in common_chars]
        s = s1 + s2
        if len(s1) == 0 and len(s2) == 0: # If all characters are removed from both strings
            return -1

        # list to string converstion
        return "".join(s)


x = Solution()
s1 = 'aacdb'
s2 = 'gafd'
print(x.concatenatedString(s1,s2))

'''
# Method-1
# Error: time limit exceeded
class Solution:
    def concatenatedString(self,s1,s2):
        for ch in s1:
            if s1.count(ch) >=1 and s2.count(ch) >=1:
                s1 = s1.replace(ch,'')
                s2 = s2.replace(ch,'')
        return s1+s2
'''        

