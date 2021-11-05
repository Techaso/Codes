# Selection Sort

ip = [78,33,45,76,32,89,39]
print("Unsorted array: ", ip)
for i in range(len(ip) - 1):
    for j in range(i+1, len(ip)):
        if ip[i] > ip[j]:
            temp = ip[i]
            ip[i] = ip[j]
            ip[j] = temp
            
print("Sorted array: ", ip)