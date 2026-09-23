def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	result = []
	for vector in a:
		if len(vector) != len(b):
			return -1
		num = 0
		for index, item in enumerate(vector):
			num += item * b[index] 
		result.append(num)
	return result