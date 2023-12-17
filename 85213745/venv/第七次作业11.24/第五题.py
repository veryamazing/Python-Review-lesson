#5.	筛选法求素数。
if __name__ == '__main__':
    # 定义一个列表，用于存储素数
    primes = []
    #确定素数最大范围
    max = int(input("请输入素数最大范围："))
    # 筛选素数
    for num in range(2, max):
        # 将小于等于根号num的素数标记为非素数
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            # 将素数添加到列表中
            primes.append(num)

    # 输出素数
    print("素数列表为：", primes)
