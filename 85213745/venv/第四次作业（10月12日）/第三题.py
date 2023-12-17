#3.	输入一个1～12间的整数，输出对应的月份名称缩写。
if __name__ == '__main__':

    # 定义月份名称缩写
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    # 输入一个1～12间的整数
    month = int(input("请输入一个1～12间的整数："))

    # 判断输入的整数是否在1～12之间
    if month < 1 or month > 12:
        print("输入的整数不在1～12之间")
    else:
        # 输出对应的月份名称缩写
        m = month
        pos = (m - 1) * 3
        monthAbbrev = months[pos:pos + 3]
        print("对应的月份名称缩写为：", monthAbbrev)
