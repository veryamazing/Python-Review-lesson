#输出1~100中偶数之和
if __name__ == '__main__':
    def sum_even_numbers():
        total = 0
        for i in range(1, 101):
            if i % 2 == 0:
                total += i
        return total


    print(sum_even_numbers())
