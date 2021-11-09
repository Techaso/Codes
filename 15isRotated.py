# Check if string A matches with string B if B is rotated by two places

class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        if len(str2) == 1:
            return 1
        if len(str2) == 2:
            return 0
        if len(str2) > 2:
            x = str2[len(str2)-2:len(str2)] + str2[0:len(str2)-2] # clockwise rotation
            y = str2[2:len(str2)] + str2[0:2] # anticlockwise rotation
            #print(x)
            #print(y)
            if str1 == x or str1 == y:
                return 1
            else:
                return 0
str1 = 'geeksforgeeks'#'amazon'
str2 = 'geeksgeeksfor'#'azonam'
x = Solution()
print(x.isRotated(str1,str2))