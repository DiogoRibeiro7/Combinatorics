def digitrange(minlen, maxlen, base=2):
   """Generator producing all lists of digits to a given base."""
   digits = [0]*maxlen
   if minlen>0: digits[minlen] = 1
   while True:
      yield digits
      digits[0] += 1
      i = 0
      while digits[i] >= base:
         if ((i+1)>= maxlen): raise StopIteration
         digits[i] = 0
         digits[i+1] += 1
         i += 1
