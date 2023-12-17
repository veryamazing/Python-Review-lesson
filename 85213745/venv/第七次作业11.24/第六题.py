if __name__ == '__main__':
    # 定义一个有序列表
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 定义要查找的元素
    x = 3

    # 定义两个变量，分别表示左右边界
    left = 0
    right = len(ls) - 1

    # 进行二分查找
    while left <= right:
        # 计算中点
        mid = (left + right) // 2
        # 如果中点等于要查找的元素，则返回该元素的下标
        if ls[mid] == x:
            print("元素{}在列表中，下标为{}".format(x, mid))
            break
        # 如果中点小于要查找的元素，则将右边界缩小一半
        elif ls[mid] < x:
            left = mid + 1
        # 如果中点大于要查找的元素，则将左边界缩小一半
        else:
            right = mid - 1
    # 如果没有找到要查找的元素，则输出提示信息
    else:
        print("元素{}不在列表中".format(x))
