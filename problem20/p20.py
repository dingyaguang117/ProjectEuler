def main():
	ans = 1
	for i in xrange(1,101):
		ans *= i
	print sum([int(c) for c in str(ans)])

if __name__ == '__main__':
	main()