def subS(s):

	subs = []
	j = 1	

	while j<len(s):
		for i in range(len(s)):
			if i+j <= len(s):
				subs.append(s[i:i+j])
			else:
				continue
		j += 1

	return len(set(subs))+1

def subStrings():
	n = input()
	strings = [raw_input() for i in range(n)]

	times = map(subS, strings)

	for t in times:
		print t

subStrings()