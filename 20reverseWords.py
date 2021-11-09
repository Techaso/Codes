# Reverse words in a given string.
class Solution:
    def reverseWords(self,S):
        output_string = ""
        word_start = 0
        for i in range(len(S)):
            if S[i] == '.':
                word = '.' + S[word_start:i] # add '.' before every word except for the last word
                output_string = word + output_string # concatenating words in reverse order
                word_start = i+1 # starting index of next word
        # last word
        word = S[word_start:]
        output_string = word + output_string
        return output_string

x = Solution()
S = 'i.like.this.program.very.much'
print(x.reverseWords(S))
