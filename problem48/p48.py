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

def main():
	ans = 0
	for i in xrange(1,1001):
		print i
		ans += FastPower(i,i,10**10)
		ans %= 10**10
	print ans
if __name__ == '__main__':
	main()