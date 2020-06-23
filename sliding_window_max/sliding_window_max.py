'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#!class range(stop: int)
# range(stop) -> range object range(start, stop[, step]) -> range object
# Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by
# step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3.
# These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).

#!def max(arg1: _T, arg2: _T, *_args: _T, key: Callable[[_T], Any]=...)
# max(iterable, *[, default=obj, key=func]) -> value max(arg1, arg2, *args, *[, key=func]) -> value
# With a single iterable argument, return its biggest item.
# The default keyword-only argument specifies an object to return if the provided iterable is empty.
# With two or more arguments, return the largest argument.


def sliding_window_max(nums, k):
    # Your code here

    window = []
    arr = [0] * k
    for i in range(0, len(nums) - k + 1):
        arr = nums[i:i + k]
        window.append(max(arr))

    return window
# test_sliding_window_max.py: Ran 3 tests in 0.000s-OK
# test_sliding_window_max_large_input.py: Ran 1 test in 24.447s- SUPER BAD!


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
