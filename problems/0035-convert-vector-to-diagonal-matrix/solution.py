import numpy as np

def make_diagonal(x):
	# Your code here
	#result = [np.zeros(len(x)).tolist()[i][i] = x[i] for i in range(len(x))]
	result = np.diag(x).tolist()
	return result
	pass