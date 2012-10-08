def FastPower(A, N):
	'''
		return A**N
	'''
	if(N == 0):return 1
	ans = FastPower(A,N/2)
	ans *= ans
	if N&1 > 0:
		ans *= A
	return ans

def main():
	print sum([int(c) for c in str(FastPower(2,100000))])

if __name__ == '__main__':
	main()