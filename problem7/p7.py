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

print PrimeList(10001)[-1]