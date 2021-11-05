# Binary search without recursion
# This is a basic version of binary search, without any edge cases like repetitions of numbers, no items in list etc
def binary_search(my_list, item):
    low = 0
    high = len(my_list)-1

    while low <= high:
        # mid and guess will be defined inside the while loop (instead of near to outsider low and high variables) otherwise mid and guess won't change and loop will keep running
        mid = int((low+high)/2)
        guess = my_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [3,5,6,8,9,13]
item = 5

# necessary to use this print function otherwise python won't show any output
print(binary_search(my_list, item))

        