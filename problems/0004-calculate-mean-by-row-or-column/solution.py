import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	arr = np.array(matrix, dtype=float)
	
	if mode == 'column':
		means = arr.mean(axis=0)
	elif mode == 'row':
		means = arr.mean(axis=1)
	else:
		raise ValueError("Not row or column")

	return means.tolist()