if __name__ == '__main__':
    def gcd(a, b):
        # 判断两个数的大小关系
        if a > b:
            # 交换两个数的大小关系
            a, b = b, a
        # 循环求解最小公倍数
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


    # 主函数
    a = int(input("请输入第一个正整数："))
    b = int(input("请输入第二个正整数："))
    print("两个正整数的最小公倍数是：", gcd(a, b))
