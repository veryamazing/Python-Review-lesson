if __name__ == '__main__':
    # 定义一个列表，用于存储素数
    primes = []

    # 筛选素数
    for num in range(1, 301):
        primes.append(num)
    print("素数列表为：", primes)

    # 将1标记为非素数
    primes[0] = -1

    # 将能被素数2整除的所有数标记为非素数
    for i in range(2, len(primes)):
        if primes[i] != -1:
            for j in range(2, int(primes[i] ** 0.5) + 1):
                if primes[i] % j == 0:
                    primes[i] = -1
                    break

    # 找到下一个素数，将能被其整除的所有数标记为非素数
    for i in range(2, len(primes)):
        if primes[i] != -1:
            for j in range(2, int(primes[i] ** 0.5) + 1):
                if primes[j] != -1 and primes[i] % j == 0:
                    primes[j] = -1

    # 过滤掉列表中的非素数(-1)
    primes = [p for p in primes if p != -1]
    # 输出素数
    print("素数列表为：", primes)
