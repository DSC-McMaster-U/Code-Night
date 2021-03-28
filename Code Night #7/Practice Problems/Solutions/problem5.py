# Solution 1
def problem4(words_list, num, letter):
    new_words_list = []
    for i in range(len(words_list)):
        if len(words_list[i]) >= num:
            new_words_list.append(words_list[i][:num - 1] + letter + words_list[i][num:])
        else:
            new_words_list.append(words_list[i])
    return new_words_list


# Solution 2
def problem4(words_list, num, letter):
    new_words_list = []
    for word in words_list:
        if len(word) >= num:
            new_words_list.append(word[:num - 1] + letter + word[num:])
        else:
            new_words_list.append(word)
    return new_words_list


print(problem4(["Hello", "Welcome", "Goodbye"], 3, "z"))
