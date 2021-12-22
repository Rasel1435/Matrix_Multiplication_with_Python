## Matrix Multiplication
mat1 = [
    [8,2],
    [9,4]
]
mat2 = [
    [1,2],
    [3,4]
]

def mat_add(mat1:list, mat2:list)->list:
    res = []
    for row in range(len(mat1)):
        Row = []
        for col in range(len(mat1[0])):
            Row.append(mat1[row][col] + mat2[row][col])
        res.append(Row)
    return res


mat_add(mat1, mat2)
