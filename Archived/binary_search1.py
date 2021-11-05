# binary search using recursion
nL = [2,3,6,8,11,17,18]
no = 1
def subBS(nL, no, low, high):
    #print("subBS")
    # print(nL, no, low, high)
    mid = int((low + high)/2)
    if low==high and nL[mid] != no:
        return "Number doesn't exist in given list"
    if nL[mid] == no:
        return mid
    elif nL[mid] > no:
        high = mid - 1
        return subBS(nL, no, low, high)
    else:
        low = mid + 1
        return subBS(nL, no, low, high)


def binarySearch(nL, no):
    #print("binarySearch")
    low = 0
    high = len(nL) - 1
    print('nL = {}, number = {}, low = {}, high = {}'.format(nL, no, low, high))
    return subBS(nL, no, low, high)

print(binarySearch(nL,no))