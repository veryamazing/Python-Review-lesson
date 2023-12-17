#编写程序，实现利用while循环输出100以内偶数的功能。
if __name__ == '__main__':
    i = 1
    while i <= 100:
        if i%2 == 0:
            print(i)
        i+=1
