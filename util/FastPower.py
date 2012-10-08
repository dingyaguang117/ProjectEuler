def FastPower(A, N, mod=None):
	'''
		return A**N
	'''
	if(N == 0):return 1
	ans = FastPower(A,N/2)
	ans *= ans
	if mod != None:
		ans %= mod
	if N&1 > 0:
		ans *= A
	if mod != None:
		ans %= mod
	return ans
