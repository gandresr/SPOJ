def isPalindrome(n):
	
	s = str(n)
	p = list(s)
	p.reverse()
	s1 = ''.join(p)

	if s==s1:
		return True
	return False

def nextPalindrome():
	n = input()
	integers = [input() for i in range(n)]
	ans = []
	for p in integers:

		s = p+1
		while not isPalindrome(s):
			s += 1
		ans.append(s)

	for a in ans:
		print a

nextPalindrome()