#统计英文句子“Life is short,we need Python."中各字符出现的次数
if __name__ == '__main__':
    sentence = "skdaskerkjsalkj"

    char_count = {}

    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)

