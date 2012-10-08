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
	return ans

def main():
	L = PrimeListFill(2000000)
	print sum(L)

if __name__ == '__main__':
	main()