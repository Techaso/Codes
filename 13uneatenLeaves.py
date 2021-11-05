# Jumping Caterpillars
#METHOD 1:
#Problem: Time Limit Exceeded
def uneatenLeaves(arr,n,k):
    leaves = []
    for i in range(n):
        leaves.append(0)
    
    for i in range(n):
        for j in range(k):
            if (i + 1) % arr[j] == 0 and leaves[i] == 0:
                leaves[i] = 1
    
    count = 0
    for i in range(n):
        if leaves[i] == 0:
            count+=1
    
    return count


n = 10
k = 3
arr = [2,3,5]
print(uneatenLeaves(arr,n,k))
