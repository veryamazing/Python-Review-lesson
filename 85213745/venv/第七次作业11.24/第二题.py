#实现判断用户输入的数是正数还是负数的功能
if __name__ == '__main__':
    num = float(input("请输入一个数："))

    if num > 0:
        print("您输入的数是正数。")
    elif num < 0:
        print("您输入的数是负数。")
    else:
        print("您输入的数是0。")
