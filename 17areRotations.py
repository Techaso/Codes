# Check if strings are rotations of each other or not
class Solution:
    def areRotations(self,s1,s2):
        if len(s1) == len(s2):
            for rotcount in range(len(s1)):
                x = s1[rotcount:len(s1)] + s1[0:rotcount]
                if x == s2:
                    return 1
            return 0

x = Solution()
s1 = 'dylsebxjwlmpamjneoehhlgayxtgs' #'geeksforgeeks'
s2 = 'lsebxjwlmpamjneoehhlgayxfgsdy' #'forgeeksgeeks'
print(x.areRotations(s1,s2))