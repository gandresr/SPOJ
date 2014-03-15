def ans2life():
	
	ans = []

	while True:
		number = input()
		if number == 42:
			break
		ans.append(number)

	for n in ans:
		print n

ans2life()