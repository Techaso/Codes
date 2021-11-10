# Remove Duplicates from string
# Method-2
class Solution:
    def removeDups(self, S):
        new_s = ""
        for v in S:
            if v not in new_s:
                new_s = new_s + v
        return new_s
        
x = Solution()
S = 'zvvo'
print(x.removeDups(S))

'''
Method-1: Correct code but GfG Issue: All inbuit converters like set(), dict etc do not work correctly in GfG
class Solution:
    def removeDups(self, S):
        str_s = ""
        set_s = dict.fromkeys(S).keys()
        #print(list(set_s))
        for ele in list(set_s): 
            str_s += ele
        return str_s
'''