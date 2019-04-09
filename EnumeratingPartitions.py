If partitions are written in decreasing order we can place them in reverse lexicographic order, so 
[6,4,2,2] < [6,5,4,2,1] < [6,5,3,3,1]. The next operator will thus search from right to left for the first pair 
differing by two or more and will transfer across that boundary. 
Here we view the list as ending in zeros.


def partitions(n):
	# base case of recursion: zero is the sum of the empty list
	if n == 0:
		yield []
		return
		
	# modify partitions of n-1 to form partitions of n
	for p in partitions(n-1):
		yield [1] + p
		if p and (len(p) < 2 or p[1] > p[0]):
			yield [p[0] + 1] + p[1:]
      
'''      
Upper bound. The number of partitions grows quickly.
'''

def upper_bound(k):
    """Ramanujan's upper bound for number of partitions of k"""
    return int(exp(pi*sqrt(2.0*k/3.0))/(4.0*k*sqrt(3.0)))

'''
TUPLE VERSION
'''

def partitions_tuple(n):
    # tuple version
    if n == 0:
        yield ()
        return

    for p in partitions_tuple(n-1):
        yield (1, ) + p
        if p and (len(p) &lt; 2 or p[1] &gt; p[0]):
            yield (p[0] + 1, ) + p[1:]
            
 '''
 REVERSE ORDER
 '''
 
 
 def partitions_rev(n):
    # reverse order
    if n == 0:
        yield []
        return

    for p in partitions_rev(n-1):
        yield p + [1]
        if p and (len(p) &lt; 2 or p[-2] &gt; p[-1]):
            yield p[:-1] + [p[-1] + 1]
