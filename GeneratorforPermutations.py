  
def genperm(theset):
   """A generator which returns the permutations of the presented set."""
   if (len(theset) <= 1): 
      yield theset
   else:
      for i in range(len(theset)):
         for restperm in genperm(theset[:i] + theset[i+1:]):
            yield [theset[i]] + restperm
