def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	det = lambda minor: (
		minor[0][0]*minor[1][1] - minor[1][0]*minor[0][1] 
		if len(minor) == 2
		else sum(
			(-1)**j*minor[0][j]*
			det([
				[value for k, value in enumerate(row) if k !=j] 
				for row in minor[1:]
			]) 
			for j in range(len(minor[0]))
		)
	)
	trace = sum([matrix[i][i] for i in range(len(matrix))])
	return det(matrix), trace