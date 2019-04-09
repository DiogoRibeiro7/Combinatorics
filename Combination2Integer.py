def choose2num(thelist):
    """ choose2num(thelist) - Given a bit vector and thinking of it as a combination (aka k-subset) from a set with n elements, return the order of this element in the list of all (n choose k) such combinations."""
    if(len([thelist[i] for i in range(len(thelist)) if ((thelist[i] != 0) and (thelist[i] != 1))]) > 0): raise ValueError("choose2num(" + thelist + ") expecting list entries {0,1}")
    n = len(thelist)
    k = sum(thelist) # total number of 1's
    if ((n==0) or (k==0) or (n==k)): 
        print "   return 0"
        return 0 # base cases of form [], [0,0,...] or [1,1,...]
    num = 0
    for firstbit in range(n-k+1):
        if (thelist[firstbit] == 1):
            return num + choose2num(thelist[firstbit+1:])
        num += binomial(n-firstbit-1,k-1)
