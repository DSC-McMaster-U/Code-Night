def problem4(matrix):
    result = 0
    for i in range(len(matrix)):
        if matrix[i] != []: # Can be shortened to 'if matrix[i]:`, achieves same result
            result += matrix[i][i]
    return result


print(problem4([[21, 53, 68], [83, 64, 69], [27, 12, 32]]))
