#Function to locate the occurrence of the string x in the string s.
def strstr(s,x):
    for i in range(len(s)):
        for j in range(len(x)):
            #print(i, s[i:i+len(x)], x)
            if s[i:i+len(x)] == x:
                return i
    return -1
s = 'GeeksForGeeks'
x = 'For'

print(strstr(s,x))