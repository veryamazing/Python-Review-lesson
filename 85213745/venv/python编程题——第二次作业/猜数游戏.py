import random as rd
if __name__ == '__main__':
    target = rd.randint(1,50)
    print("已产生一个1~50之间的随机数，猜数值")
    count = 0
    while True:
        guess = eval(input("请输入猜测的数值："))
        count += 1
        if guess > target:
            print("太大了")
        elif guess <target:
            print("太小了")
        else:
            print("好棒，猜{}次就中了！".format(count))
            break