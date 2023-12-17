if __name__ == '__main__':
    def factorial():
        result = 1
        for i in range(20, 2, -1):
            result *= i
        return result

    print(factorial())
