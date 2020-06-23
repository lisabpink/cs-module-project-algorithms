'''
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?

if the left pointer "sees" a zero and the right pointer "sees" a non-zero
swap

if the left sees a non-zero increment
if the right sees a zero increment
'''


def moving_zeroes(arr):
    # left pointer at the beginning
    # right pointer at the end

    # loop until left and right pointers meet or right pointer passes the left pointer
    # swap situation:
    # left sees zero and right sees non-zero
    # swap the items
    # increment left
    # decrement right
    # non-swap situation
    # if left sees non-zero
    # increment left
    # if right sees zero
    # decrement right

    return arr
