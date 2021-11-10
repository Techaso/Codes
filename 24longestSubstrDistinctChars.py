# Longest Distinct characters in string
# Method-2: Shifting start_index by 1 whenever a character repeats, and start loop from this start_index, instead of contueing from the current index where the character repeats
class Solution:
    def longestSubstrDistinctChars(self, S):
        start_index = 0
        dist_string = ''
        count = 0
        max_count = 0
        i = 0
        while i < len(S):
            
            if S[i] not in dist_string:
                dist_string += S[i]
                count +=1
                if count > max_count:
                    max_count = count
                    #print(dist_string)
                i+=1
            else:
                start_index +=1
                i = start_index
                count = 0
                dist_string = ''
        return max_count

x = Solution()
S = 'geeksforgeeks' #'aldshflasghdfasgfkhgasdfasdgvfyweofyewyrtyefgv' #'aewergrththy'
print(x.longestSubstrDistinctChars(S))
'''
# Method-1: Error: test cases failing because when character is repeating we're not starting from just the next character of the character where previous counting started
class Solution:
    def longestSubstrDistinctChars(self, S):
        dist_string = ''
        count = 0
        max_count = 0
        for v in S:
            if v not in dist_string:
                dist_string += v
                count +=1
                if count > max_count:
                    max_count = count
                    #print(dist_string)
            else:
                count = 1
                dist_string = ''+v
        return max_count

x = Solution()
S = 'aewergrththy'#'aldshflasghdfasgfkhgasdfasdgvfyweofyewyrtyefgv'
print(x.longestSubstrDistinctChars(S))
'''