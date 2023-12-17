if __name__ == '__main__':
    import random

    random_list = []

    for i in range(20):
        num = random.randint(0, 20)
        random_list.append(num)

    print("生成的随机数有：",random_list)
    random_list = list(set(random_list))

    print("其中出现的有：",random_list)

