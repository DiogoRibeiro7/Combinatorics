def list2int(thelist,base=2):
   """Return the integer whose digits are listed."""
   return reduce(lambda x,y:base*x+y,reversed(thelist),0
