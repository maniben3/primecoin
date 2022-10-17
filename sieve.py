import time
import numpy as np
from numba import njit
start=time.time()
@njit
def n(primes,inv,max):
 res=np.full(max+10**6,True)
 for p,q in zip(primes,inv):
  for i in range (0,max,p):
   x=i+q
   res[x]=False
 r=[]
 for i in range(109375000):
    if res[i] and res[2*i] and res[4*i] and res[8*i] and res[16*i] and res[32*i]:
      r.append(i)
 return r
print(time.time()-start)
