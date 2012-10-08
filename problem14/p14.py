MAX = 200000000
dp = [0]*(MAX+1)

def calc(n):

	if n <= MAX :
		if dp[n] != 0:
			return dp[n]

	if n&1 == 0:
		r = calc(n>>1)+1
	else:
		r = calc(n*3+1)+1

	if  n <= MAX:
		dp[n] = r
	return r

def main():
	m = 1
	dp[1] = 1
	for i in xrange(2,1000001):
		if calc(i) > m:
			m = calc(i)
			ans = i
	print ans

if __name__ == '__main__':
	main()