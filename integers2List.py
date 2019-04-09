def int2list(num,listlen=0,base=2):
   """Return a list of the digits of num, zero padding to produce a list of length at least listlen, to the given base (default binary)"""
   digits = []; temp = num
   while temp>0:
      digits.append(temp % base)
      temp = temp // base
   digits.extend((listlen-len(digits))*[0])
   return digits
   
   
   
### with list compression
def int2list2(num,listlen=0,base=2):
   """Return a list of the digits of num, zero padding to produce a list of length at least listlen, to the given base (default binary)"""
   return [(num//base**i)%base for i in range(max(listlen,int(math.ceil(math.log(num,base)))))]
