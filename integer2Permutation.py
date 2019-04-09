####Recursive Algorithm:  
def num2perm(num,thelist):
    if len(thelist) <= 1: return thelist
    num = num % math.factorial(len(thelist))
    nextelt = thelist[num // math.factorial(len(thelist)-1)]
    return [nextelt] + num2perm(num, [x for x in thelist if x!=nextelt])



#########Iterative Algorithm:  
def num2perm2(num,permlen):
    theperm = []
    num = num % math.factorial(permlen)
    theelts = range(permlen)
    for i in range(1,permlen):
        thedigit = (num // math.factorial(permlen-i))
        num = (num % math.factorial(permlen-i))
        theperm += [theelts[thedigit]]
        theelts = theelts[:thedigit] + theelts[thedigit+1:]
    return theperm + theelts
