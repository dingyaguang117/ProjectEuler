import sys
import os
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from util.Prime import GetIntegerMapFactorization

def calc(facs):
	num = 1
	for key in facs:
		num *= facs[key]+1
	return num

def main():
	i = 0
	n = 0
	fac = GetIntegerMapFactorization(100000000)
	while True:
		i += 1
		n += i
		if calc(fac(n)) > 500:
			print n
			break
if __name__ == '__main__':
	main()
