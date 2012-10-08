import sys
import os
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from util.Prime import GetIntegerFactorization
from util.Combination import CombinationMatrix



def main():
	c = CombinationMatrix(50)
	l = set(reduce(lambda a,b:a+b,c))
	IntegerFactorization = GetIntegerFactorization(max(l))
	ans = 0
	print l
	for num in l:
		pl = IntegerFactorization(num)
		if len(set(pl)) == len(pl):
			ans += num

	print ans

if __name__ == '__main__':
	main()
