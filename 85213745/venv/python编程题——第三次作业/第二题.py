#已知某煤场有29.5顿煤，先用一辆载重4顿的汽车运3次，
# 剩下的用一辆载重为2.5顿的汽车运送，
# 请计算还需要运送几次才能送完？
if __name__ == '__main__':

    # 定义汽车的运输能力
    car_capacity = 2.5

    # 定义煤的总量
    total_coal = 29.5

    # 计算需要运输的总次数
    total_trips = (total_coal - 4 *3 )// car_capacity

    # 输出结果
    print("需要运输", total_trips, "次才能送完")
