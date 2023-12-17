#4.	编写一个程序，模拟掷两个骰子100000次，统计各点数出现的概率。
if __name__ == '__main__':
    import random

    # 定义一个列表，用于存储每个点数出现的次数
    dice_counts = [0] * 13

    # 模拟掷骰子100000次
    for i in range(100000):
        # 随机生成两个骰子的点数
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        # 将点数相加，得到总点数
        total_dice = dice1 + dice2
        # 将总点数加1，统计每个点数出现的次数
        dice_counts[total_dice] += 1

    # 输出每个点数出现的概率
    for i in range(1, 13):
        probability = dice_counts[i] / 100000
        print("点数为{}的概率为：{:.2f}%".format(i, probability * 100))
