import math

def PrimeList(N = None,limit = None):
	'''
		return first N primes or  primes <= limit
	'''
	if N ==None and limit ==None:
		raise Exception('need either N or limit')
	ans = [2,3]
	i = 5
	dt = 2
	while True:
		if N != None and len(ans) >= N : break
		if limit != None and ans[-1] >= limit: break 
		f = True
		for j in ans:
			if i%j == 0:
				f = False
				break
		if f:
			ans.append(i)
		i += dt
		dt = 6 - dt
	return ans


def PrimeListFill(limit):
	'''
		return primes <= limit
	'''
	A = [True] * (limit + 1)
	plist = PrimeList(limit=int(math.sqrt(limit)))
	for p in plist:
		n = 2 * p
		while n <= limit:
			A[n] = False
			n += p
			
	ans = []
	for i in xrange(2,len(A)):
		if A[i]:
			ans.append(i)
	return ans,A

def GetIntegerFactorization(N):
	'''
		N is the max Integer supposed to Fac
	'''
	plist = PrimeListFill(limit=int(math.sqrt(N)))
	def IntegerFactorization(N):
		n = N
		ans = []
		while n > 1:
			f = False
			for p in plist:
				if n % p == 0:
					ans.append(p)
					n /= p
					f = True
					break
			if not f:
				ans.append(n)
				break
		return ans
	return IntegerFactorization


def GetIntegerMapFactorization(N):
	'''
		N is the max Integer supposed to Fac
	'''
	plist = PrimeListFill(limit=int(math.sqrt(N)))
	def IntegerFactorization(N):
		n = N
		ans = {}
		while n > 1:
			f = False
			for p in plist:
				if n % p == 0:
					if p not in ans:
						ans[p] = 1
					else:
						ans[p] += 1
					n /= p
					f = True
					break
			if not f:
				ans[n] =1
				break
		return ans
	return IntegerFactorization

#print PrimeListFill(100000)
#print GetIntegerFactorization(100000)(1009)
#print GetIntegerMapFactorization(100000)(1007)

