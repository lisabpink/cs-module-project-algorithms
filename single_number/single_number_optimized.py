def single_number_optimized(nums): # O(n)
    # keep track of number of times an item occurs in input
    counts = {}

    # loop through input list O(n)
    for num in nums:
        # if item in counts
        if num in counts:
            # remove item
            del counts[num]
        # otherwise
        else:
            counts[num] = 1
            # add item

    for k, v in counts.items(): # O(1)
        if v == 1:
            return k