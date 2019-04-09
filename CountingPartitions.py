'''
The function which gives the number of distinct partitions of the integer n is referred to as the partition P function, p(n). 
Rather than computing this directly, we will work with the function p(n,k), the number of partions of n whose largest component is k. 
Obviously p(n) is equal to the sum of p(n,k) for all k smaller than n. Any partition in p(n,k) 
comes from a partion in p(n-k) by just ignoring the first component. Thus we get a recursive algorithm for computing p(n):
'''


def partitionp(n,k=-1):
    """ partitionp(n) is the number of distinct unordered partitions of the integer n.
    partitionp(n,k) is the number of distinct unordered partitions of the integer n whose largest component is k."""
    if (k == -1): return sum([partitionp(n,i) for i in range(1,n+1)])
    if (n < k): return 0
    if ((n==0) or (n==1)): return 1 # base cases, {0} and {1}
    if ((k == 1) or (n == k)): return 1 # base cases, {1+1+...} and {n}
    return sum([partitionp(n-k,i) for i in range(1,min(k,n-k)+1)])

'''
A much more efficient approach is via an approach called dynamic programming. Here we compute a function psum(n,k), 
which is the total number of n-partitions with largest component of k or smaller. 
At any given stage we will have computed the values of psum(1,k), psum(2,k), psum(3,k), ..., psum(n,k) 
for some fixed k. Given this vector of n values we compute the values for k+1 as follows:
'''


def partitionp(n):
    partpsum = [1]*(n+1)
    for i in range(2,n+1):
        for j in range(i,n+1):
            partpsum[j] += partpsum[j-i]
    return partpsum[n]
