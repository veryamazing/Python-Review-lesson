if __name__ == '__main__':
    # num_one = 12
    #
    #
    # def sum(num_two):
    #     global num_one
    #     num_one = 90
    #     return num_one + num_two
    #
    #
    # print(sum(10))
    def many_param(num_one, num_two, *args):
        print(args)


    many_param(11, 22, 33, 44, 55)
