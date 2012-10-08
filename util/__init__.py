def f():
	for i in xrange(10):
		yield i

	for i in xrange(5):
		yield '1%s'%i


for one in f():
	print one			