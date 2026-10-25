def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	[[a,b], [c,d]] = matrix
	det = a*d-c*b
	trace = a+d
	eigen_one = (trace + ((trace)**2 - 4 * det)**(1/2))/2
	eigen_two = (trace - ((trace)**2 - 4 * det)**(1/2))/2
	return [eigen_one, eigen_two]