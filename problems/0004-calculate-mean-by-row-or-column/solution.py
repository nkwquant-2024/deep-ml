def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		matrix_t = matrix
	else:
		matrix_t = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
	
	means = [sum(i)/len(i) for i in matrix_t]
	return means