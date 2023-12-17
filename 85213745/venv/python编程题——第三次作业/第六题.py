if __name__ == '__main__':
    a = float(input("请输入a= "))
    b = float(input("请输入b= "))
    print("a=%f,b=%f"%(a,b))
    a , b = b , a
    print("交换后结果a = %f,b = %f"%(a,b))
