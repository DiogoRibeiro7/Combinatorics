def perm2num(theperm):
   permlen = len(theperm)
   theelts = range(permlen)
   num = 0
   for i in range(permlen):
      thedigit = theelts.index(theperm[i])
      num += thedigit*math.factorial(permlen-i-1)
      del theelts[thedigit]
   return num
