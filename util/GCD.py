def GCD(L):
	if len(L) > 2:
		return GCD([L[0], GCD(L[1:])])
	a = max(L)
	b = min(L)
	while a % b != 0:
		t = b
		b = a % b
		a = t
	return b

def LCM(L):
	if len(L) > 2:
		return LCM([L[0],LCM(L[1:])])
	return L[0] * L[1] / GCD(L)

print GCD(range(1,21))
print LCM(range(1,21))