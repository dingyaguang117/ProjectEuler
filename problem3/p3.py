import math
def PrimeList(N = None,limit = None):
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

def IntegerFactorization(N):
	pass


def main():
	N = 600851475143
	a = math.sqrt(N)
	print a
	plist = PrimeList(limit=a)[::-1]
	for p in plist:
		if N % p == 0:
			print p
			break


if __name__ == '__main__':
	main()