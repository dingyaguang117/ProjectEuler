import sys
import os
sys.path += [os.path.dirname(os.path.dirname(__file__))]
from util.Prime import PrimeListFill
from util.Prime import PrimeList


PL,PM = PrimeListFill(100000000)
PL.pop(0)
PL.pop(1)
print PL[-1],len(PL)
m = []
msum = 0

ans = 1000000000000

def calc(p):
	global ans
	global m
	global msum
	global PL
	global PM

	if p>= len(PL):
		return
	if len(m) == 5:
		if msum < ans:
			ans = msum
		return
	for i in xrange(p,1000):
		num = PL[i]
		if msum + num > ans:
			break

		flg = True
		for key in m:
			snum = str(num)
			skey = str(key)
			if not PM[int(snum+skey)] or not PM[int(skey+snum)]:
				flg = False
				break
		if flg:
			m.append(num)
			msum += num
			calc(i+1)
			m.pop(len(m)-1)
			msum -= num



def main():
	calc(0)
	print PL[1000]
	print ans


if __name__ == '__main__':
	main()
