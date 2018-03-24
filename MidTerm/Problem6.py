def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if (N != 0):
        return (N % 10 + sumDigits(N // 10))
    else:
       return 0
