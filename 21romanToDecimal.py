# Roman to integer conversion
'''
RULES:
# When a bigger letter precedes a smaller letter, the letters are added. For example: LI, L > I, so LI = L + I = 50 + 1 = 51.
# When a smaller letter precedes a bigger letter, the letters are subtracted. For example: IX, I < X, so IX = X - I = 10 - 1 = 9.
# When a letter is repeated multiple times, they get added. For example: XX = X + X = 10 + 10 = 20
# The same letter cannot be used more than three times in succession.
'''
class Solution:
    def romanToDecimal(self, S):
        # converting roman character to integer number
        def charToValue(roman_char):
            if roman_char == 'M':
                no = 1000
            if roman_char == 'D':
                no = 500
            if roman_char == 'C':
                no = 100
            if roman_char == 'L':
                no = 50
            if roman_char == 'X':
                no = 10
            if roman_char == 'V':
                no = 5
            if roman_char == 'I':
                no = 1
            return no

        count = 0
        i = 0
        if len(S)>1:
            while i<len(S)-1:
                curr_no = charToValue(S[i])
                next_no = charToValue(S[i+1])
                #Conversion Rules
                if curr_no >= next_no:
                    if i == len(S)-2: #reached to second last digit
                        count += (curr_no + next_no)
                        return count
                    else:
                        count += curr_no
                        i+=1
                else:
                    count += (next_no-curr_no)
                    i+=2
                    if i == len(S)-1: #reached to last digit
                        curr_no = charToValue(S[i]) #Get integer value of last roman digit
                        count += curr_no
                        return count
            return count

        # only one roman digit given in the input
        else:
            curr_no = charToValue(S[i])
            return curr_no
x = Solution()
S='DCCI'
print(x.romanToDecimal(S))
