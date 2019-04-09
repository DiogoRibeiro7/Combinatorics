###Multiplicative Formula: 
def binomial(n,k):
   """Compute n factorial by a direct multiplicative method."""
   if k > n-k: k = n-k  # Use symmetry of Pascal's triangle
   accum = 1
   for i in range(1,k+1):
      accum *= (n - (k - i))
      accum /= i
   return accum
              
###Additive Formula:  
def binomial2(n,k):
   """Compute n factorial by an additive method."""
   if k > n-k: k = n-k  # Use symmetry of Pascal's triangle
   thediag = [i+1 for i in range(k+1)]
   for i in range(n-k-1):
      for j in range(1,k+1):
         thediag[j] += thediag[j-1]
   return thediag[k]
