def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        c = -1
    else:
        row_dim, col_dim, sum_dim = len(a), len(b[0]),len(b)   
        c = [[sum(a[i][k]*b[k][j] for k in range(sum_dim))  for j in range(col_dim)] for i in range(row_dim)]
    return c