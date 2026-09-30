def transpose(mat):
    # если матрица пустая, возвращаю пустой список
    if len(mat) == 0:
        return []
    # проверка на прямоугольность матрицы
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("рваная матрица")
    res = []
    # прохожусь по столбцам
    for j in range(row_length):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        res.append(new_row)
    return res


def row_sums(mat):
    # если матрица пустая, возвращаю пустой список
    if len(mat) == 0:
        return []
    # проверка на прямоугольность матрицы
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("рваная матрица")
    res = []
    for row in mat:
        sum_row = 0 
        for num in row:
            sum_row += num
        res.append(sum_row)
    return res


def col_sums(mat):
    # если матрица пустая, возвращаю пустой список
    if len(mat) == 0:
        return []
    # проверка на прямоугольность матрицы
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("рваная матрица")
    res = []
    for j in range(row_length):
        summ_col = 0 
        for i in range(len(mat)):
            summ_col += mat[i][j]
        res.append(summ_col)
    return res


a1 = [[1, 2, 3]]
a2 = [[1], [2], [3]]
a3 = [[1, 2], [3, 4]]
a4 = []
a5 = [[1, 2], [3]]

# print(transpose(a1))
# print(transpose(a2))
# print(transpose(a3))
# print(transpose(a4))
# print(transpose(a5))

b1 = [[1, 2, 3], [4, 5, 6]]
b2 = [[-1, 1], [10, -10]] 
b3 = [[0, 0], [0, 0]]
b4 = [[1, 2], [3]]

# print(row_sums(b1))
# print(row_sums(b2))
# print(row_sums(b3))
# print(row_sums(b4))

print(col_sums(b1))
print(col_sums(b2))
print(col_sums(b3))
print(col_sums(b4))