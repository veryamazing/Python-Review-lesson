#商店需要找钱给顾客，
# 现在只有50元、5元、1元的人民币若干张。
# 输入一个整数金额值，给出找钱方案
if __name__ == '__main__':

    # 定义可用的钱币面值和数量
    denominations = [50, 5, 1]
    quantities = [0, 0, 0]

    # 输入需要找钱的金额
    amount = int(input("请输入需要找钱的金额："))

    # 计算需要找的钱币数量
    for i in range(len(denominations)):
        quantities[i] = amount // denominations[i]
        amount = amount % denominations[i]

    # 输出找钱方案
    print("找钱方案如下：")
    for i in range(len(denominations)):
        if quantities[i] > 0:
            print(quantities[i], "张", denominations[i], "元")
