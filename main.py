import sieve
primes = []
def simpleSieve(limit):
	mark =np.full(limit+1,True)
	p = 2
	while (p * p <= limit):
		if (mark[p] == True):
			for i in range(p * p, limit + 1, p):
				mark[i] = False
		p += 1
	for p in range(2, limit):
		if mark[p]:
			primes.append(p)
def inverse(hash,p):
      return pow(hash, p-2, p)
inv  = []
for p in primes:
    x = inverse(hash,p)
    inv.append(x)
