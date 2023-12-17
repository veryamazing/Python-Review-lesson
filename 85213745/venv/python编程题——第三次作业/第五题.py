#输入直角三角形的两个直角边的长度a、b，求斜边c的长度
if __name__ == '__main__':
    #定义两条边a，b
    a = float(input("输入一条直角边："))
    b = float(input("输入另一条直角边："))
    #求出斜边
    c = (a**2 + b**2)**0.5
    print("斜边长度是：%f"%c)