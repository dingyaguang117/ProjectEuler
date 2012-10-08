#|Fn+1| = |1 1| * |Fn  |
#|Fn  |   |1 0|   |Fn-1|
#
#|Fn+1| = (|1 1|)**n * |F1|
#|Fn  |   (|1 0|)      |F0|

class matrix:
	def __init__(self,data):
		self.data = data

	def multiple(self, m2):
		N = len(self.data)
		if isinstance(m2,matrix):
			m2 = m2.data
		new = []
		for i in range(N):
			new.append([0]*N)
		for i in range(N):
			for j in range(N):
				for k in range(N):
					new[i][j] += self.data[i][k]*m2[k][j]
		return matrix(new)

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return str(self.data)

class Fibonacci():
	def __init__(self,N):
		fac = matrix([[1,1],[1,0]])
		self.base = []
		for i in range (N-1):
			self.base.append(fac)
			fac = fac.multiple(fac)

	def get(self,N):
		i = 0
		a = matrix([[1,0],[0,1]])
		while N > 0:
			if N&1 > 0:
				a = a.multiple(self.base[i])
			N >>= 1
			i+=1
		return a.data[1][0]+a.data[1][1]