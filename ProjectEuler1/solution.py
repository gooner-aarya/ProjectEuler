def find_sum():
	s = 0
	for i in range (1,1000):
		if i % 3 == 0:
			s += i
			continue
		if i % 5 == 0:
			s += i
			continue
	return s

print(find_sum())