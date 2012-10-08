def main():
	for a in xrange(1,1001):
		b = a
		while a*a + b*b <= (1000-a-b)**2:
			if a*a + b*b == (1000-a-b)**2:
				print a,b,1000-a-b
				print a*b*(1000-a-b)
			b += 1

if __name__ == '__main__':
	main()