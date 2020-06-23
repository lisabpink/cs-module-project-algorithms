'''
Input: an integer
Returns: an integer
'''
# USE Dictionaries via cache: A dictionary is like a list, but more general.
# In a list, the indices are required to be integers; in a dictionary they can be (almost) any type.


def eating_cookies(n, cache=None):
    print(n)
    if n == 0:
        return 1
    if n < 0:
        return 0
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
