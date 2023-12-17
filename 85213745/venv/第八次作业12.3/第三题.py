if __name__ == '__main__':
    def is_palindrome(num):
        # 将数字转换为字符串
        num_str = str(num)
        # 定义两个指针，分别指向字符串的第一个和最后一个字符
        left = 0
        right = len(num_str) - 1
        # 循环遍历字符串中的每个字符
        while left < right:
            # 如果左右指针指向的字符不同，则不是回文数
            if num_str[left] != num_str[right]:
                return False
            # 否则，将左右指针分别向中间移动一位
            left += 1
            right -= 1
        # 如果循环结束后，左右指针相遇，则是回文数
        return True


    # 主函数
    num = input("请输入数字：")
    if is_palindrome(num):
        print(num, "是回文数")
    else:
        print(num, "不是回文数")
