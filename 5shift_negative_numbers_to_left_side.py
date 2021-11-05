# Shift all the negative numbers to the left side and positive numebers to the right side, with constant extra space
def shift(arr):
    neg_index = 0 # Index for stored negative numbers on the left side
    for i in range(len(arr)):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[neg_index]
            arr[neg_index] = temp
            neg_index +=1
    return arr

x = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(shift(x))