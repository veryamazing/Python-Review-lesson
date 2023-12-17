#实现利用while循环输出100以内偶数的功能
if __name__ == '__main__':
    count = 1
    while count <= 100:
        if count % 2 == 0:
            print(count)
        count += 1
