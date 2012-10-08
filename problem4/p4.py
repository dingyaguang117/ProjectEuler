
def main():
	ans = 0
	for i in xrange(100,1000):
		for j in xrange(100,1000):
			v = i * j
			d = str(v)
			e=d[::-1]
			if d == e:
				if v > ans:
					ans = v
	print ans


if __name__ == '__main__':
	main()