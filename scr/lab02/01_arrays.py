def min_max(nums):
    if nums: 
        res = sorted(nums)
        return res[0], res[-1]
    else:
        raise ValueError

    
def unique_sorted(nums):
    unique_nums = list(set(nums)) 
    for i in range(len(unique_nums)): 
        for j in range(i + 1, len(unique_nums)):
            if unique_nums[i] > unique_nums[j]:
                unique_nums[i], unique_nums[j] = unique_nums[j], unique_nums[i]

    return unique_nums 


def flatten(mat):
    res = []
    for row in mat: 
        if not isinstance(row, (list, tuple)):
            raise TypeError("строка не является строкой матрицы")
        for numb in row:
            res.append(numb)
    return res


a1 = [3, -1, 5, 5, 0]
a2 = [42]
a3 = [-5, -2, -9]
a4 = []
a5 = [1.5, 2, 2.0, -3.1]

b1 = [3, 1, 2, 1, 3]
b2 = []
b3 = [-1, -1, 0, 2, 2]
b4 = [1.0, 1, 2.5, 2.5, 0]

c1 = [[1, 2], [3, 4]]
c2 = [[1, 2], (3, 4, 5)]
c3 = [[1], [], [2, 3]]
c4 = [[1, 2], "ab"]

# print(min_max(a1))
# print(min_max(a2))
# print(min_max(a3))
# print(min_max(a5))
# print(min_max(a4))


# print(unique_sorted(b1))
# print(unique_sorted(b2))
# print(unique_sorted(b3))
# print(unique_sorted(b4))

# print(flatten(c1))
# print(flatten(c2))
# print(flatten(c3))
# print(flatten(c4))