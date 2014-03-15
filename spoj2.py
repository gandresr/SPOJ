from math import sqrt

def isPrime(n):
	if n < 2:
		return	False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

def primes():
	
	number = input()
	ans = []
	for i in range(number):
		l = map(int,raw_input().split())
		ans.append(filter(isPrime, range(l[0],l[1]+1)))
	for a in ans:
		for prime in a:
			print prime
		print '\n',

primes()



