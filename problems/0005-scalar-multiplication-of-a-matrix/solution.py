import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = np.array(matrix, dtype=float)*scalar
	return result.tolist()
	