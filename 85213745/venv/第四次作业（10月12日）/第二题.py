#2.	编写程序，
# 检查字符串" Life is short. I use python"中是否包含字符串"python"，
# 若包含则替换为"Python"后输出新字符串，否则输出原字符串。
if __name__ == '__main__':
    original_string = " Life is short. I use python"
    new_string = original_string

    if "python" in new_string:
        new_string = new_string.replace("python", "Python")

    print(new_string)
#我们首先定义了一个原始字符串original_string，
# 然后将其赋值给一个新的变量new_string，以便在条件语句中进行检查和替换。
# 接下来，使用in关键字检查新字符串中是否包含子字符串"python"。
# 如果包含，则使用replace()方法将其替换为"Python"。
# 最后，打印出新字符串。