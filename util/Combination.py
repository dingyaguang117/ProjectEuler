def CombinationMatrix(N):
	ans = [[1],[1,1]]
	for i in xrange(2,N+1):
		one = [1]
		for j in xrange(1,i):
			one.append(ans[i-1][j-1]+ans[i-1][j])
		one.append(1)
		ans.append(one)
	return ans

#print CombinationMatrix(5)
