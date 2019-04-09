 def num2choose(num,n,k):
    """ num2choose(num,n,k) - from a list of the k-subsets (combinations) from a set with n elements, return the numth element.  Represent the combination as a bit vector."""
    if (n < k) or (k < 0): raise ValueError("num2choose: " + str(n) + ", " + str(k))
    if (n==k): return [1]*n  # base case of form [1,1,...]
    if (k==0): return [0]*n  # base case of form [0,0,...]
    num %= binomial(n,k)
    thedigit = 0
    sum = 0
    for thedigit in range(n-k+1):
        oldsum = sum
        sum += binomial(n-1-thedigit,k-1)
        if (num < sum):
            return [0]*thedigit + [1] + num2choose(num-oldsum, n-(thedigit+1),k-1)
