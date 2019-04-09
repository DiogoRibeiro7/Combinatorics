def partitionp(n,k=-1):
    """ partitionp(n) is the number of distinct unordered partitions of the integer n.
    partitionp(n,k) is the number of distinct unordered partitions of the integer n whose largest component is k."""
    if (k == -1): return sum([partitionp(n,i) for i in range(1,n+1)])
    if (n < k): return 0
    if ((n==0) or (n==1)): return 1 # base cases, {0} and {1}
    if ((k == 1) or (n == k)): return 1 # base cases, {1+1+...} and {n}
    return sum([partitionp(n-k,i) for i in range(1,min(k,n-k)+1)])
