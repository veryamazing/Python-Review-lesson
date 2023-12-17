#编写程序，实现输出100以内质数的功能。
if __name__ == '__main__':
    count = 0
    num = 2

    while count < 100:
        flag = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = True
                break
        if not flag:
            print(num)
            count += 1
        num += 1

