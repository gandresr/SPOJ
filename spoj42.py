def rev(n):
	r = list(str(n))
	r.reverse()
	return int(''.join(r))

def sumRev():
	number = input()
	numbers = []

	for i in range(number):
		l = map(int,raw_input().split())
		numbers.append(sum(map(rev, l)))

	for rs in numbers:
		print rev(rs)

sumRev()