# Check whether two given strings are an anagram of each other or not.
# An anagram of a string is another string that contains the same characters, only the order of characters can be different.
# For example, “act” and “tac” are an anagram of each other.

# from typing import Counter
class Solution:
    def isAnagram(self,a,b):
        # sorted() is an inbuilt function which does not modify the original string, but returns sorted string.
        # Method-3: use Counter(), if Counter(a) == Counter(b) or not --> Counter() function counts all the frequencies of characters in string, ==> from typing import Counter
        if sorted(a) == sorted(b):
            return True
        else:
            return False

x = Solution()
a = 'swalrl'
b = 'lsrasw'
print(x.isAnagram(a,b))       
'''
Method-2: Failing attached test case
class Solution:
    def isAnagram(self,a,b):
        if len(a) == len(b):
            new_a = ''
            new_b = ''
            # Unique values of a and b in new_a and new_b respectively
            for v in a:
                if v not in new_a:
                    new_a += v
            for v in b:
                if v not in new_b:
                    new_b += v
            print(new_a, new_b, len(new_a), len(new_b))
            # Check if new unique strings contain same unique characters or not
            if len(new_a) == len(new_b):
                for i in range(len(new_a)):
                    if new_a[i] not in new_b or new_b[i] not in new_a:
                        return 0
                return 1
            else:
                return 0
        else:
            return 0

x = Solution()
a = 'swalrl'
b = 'lsrasw'
print(x.isAnagram(a,b))
'''

'''
Method-1: Correct code but GfG Issue: All inbuit converters like set(), dict etc do not work correctly in GfG
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
'''