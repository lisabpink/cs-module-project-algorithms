def eating_cookies(n):
    '''
    Naive recursive brute-force solution
    O(3^n) time, O(3^n) space
    '''
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)