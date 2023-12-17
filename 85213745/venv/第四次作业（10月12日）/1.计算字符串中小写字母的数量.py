if __name__ == '__main__':
    s = 'AbcDeFGhIJ'
    lowercase_count = 0

    for char in s:
        if char.islower():
            lowercase_count += 1

    print("The number of lowercase characters in the string is:", lowercase_count)
#首先定义一个字符串s，
# 然后定义了一个变量lowercase_count来存储小写字符的数量。
# 接下来，我们使用一个循环遍历字符串中的每个字符，如果字符是小写字母，
# 则将lowercase_count加1。最后，我们打印出小写字符的数量。