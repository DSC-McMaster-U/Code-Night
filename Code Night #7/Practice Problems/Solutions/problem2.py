# Solution 1
def problem2(num_list):
    num_list.sort(reverse=True)
    result = ""
    for num in num_list:
        result += str(num)
    return int(result)


# Solution 2
def problem2(num_list):
    result = ""
    while len(num_list) > 0:
        next_num = max(num_list)
        result += str(next_num)
        num_list.remove(next_num)
    return int(result)


print(problem2([1, 7, 2]))
