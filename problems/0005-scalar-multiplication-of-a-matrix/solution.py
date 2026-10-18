def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	pass
	result = [[scalar * x for x in v] for v in matrix]
	return result