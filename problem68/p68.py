import sys
import os
import time
ans = '0'

def calcAns(A,B):
	min =100
	p = 0
	for i,num in enumerate(B):
		if num < min:
			min = num
			p = i
	ans = ''
	for i in xrange(5):
		ans += str(B[(p+i)%5]) + str(A[(p+i)%5]) + str(A[(p+i+1)%5])
	return ans
		

def calcB(A,B):
	if len(A) < 3:
		return
	sum = 10 + A[0] + A[1]
	r = sum - A[-1] - A[-2]
	if r in A or r in B or r<1 or r>9:
		return False
	B.append(r)
	if len(A) == 5:
		r = sum - A[0] - A[4]
		if r in A or r in B or r<1 or r>9:
			B.pop(len(B)-1)
			return False
		B.append(r)

def deCalcB(A,B):
	if len(A) < 3:
		return
	B.pop(len(B)-1)
	if len(A) ==5:
		B.pop(len(B)-1)

def calc(A,B):
	global ans
	if len(A) == 5:
		r =  calcAns(A,B)
		if r > ans:
			ans = r
		return
	for i in xrange(1,10):
		if i in A or i in B:
			continue
		A.append(i)
		if calcB(A,B) == False:
			A.pop(len(A)-1)
			continue
		calc(A,B)
		deCalcB(A,B)
		A.pop(len(A)-1)
		

def main():
	t1 = time.time()
	global ans
	calc([],[10])
	print ans
	print time.time()-t1


if __name__ == '__main__':
	main()
