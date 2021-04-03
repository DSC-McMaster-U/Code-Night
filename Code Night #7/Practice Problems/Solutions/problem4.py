def problem4(matrix):
    result = 0
    for i in range(len(matrix)):
        if matrix[i] != []: # Can be shortened to 'if matrix[i]:`, achieves same result
            result += matrix[i][i]
    return result


# Test case
print(problem4([[0, 1, 1], [2, 0, 2], [3, 3, 0]]))
