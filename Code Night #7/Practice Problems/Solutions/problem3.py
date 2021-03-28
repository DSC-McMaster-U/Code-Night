def problem3(num_list, quotient):
    for dividend in num_list:
        for divisor in num_list:
            if divisor == 0:
                pass
            elif dividend / divisor == quotient:
                return True
    return False


print(problem3([264, 92, 35, 24, 421], 11))
