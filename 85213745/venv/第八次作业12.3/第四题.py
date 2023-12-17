if __name__ == '__main__':
    def is_triangle(a, b, c):
        # 判断三角形的三边长是否都大于0
        if a > 0 and b > 0 and c > 0:
            # 判断三角形的三角形面积是否等于三个边长的乘积
            if a + b > c and b + c > a and c + a > b:
                return True
        return False


    # 主函数
    a = int(input("请输入第一个边长："))
    b = int(input("请输入第二个边长："))
    c = int(input("请输入第三个边长："))
    if is_triangle(a, b, c):
        print("这三个边长可以构成一个三角形")
    else:
        print("这三个边长不能构成一个三角形")
