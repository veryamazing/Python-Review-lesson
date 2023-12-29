if __name__ == '__main__':
    import numpy as np
    from sklearn.linear_model import LinearRegression

    # 输入数据
    cost = np.array([400, 450, 486, 500, 510, 525, 540, 549, 558, 590, 610, 640, 680, 750, 900]).reshape((-1, 1))
    profit = np.array([80, 89, 92, 102, 121, 160, 180, 189, 199, 203, 247, 250, 259, 289, 356])

    # 创建线性回归模型
    model = LinearRegression()

    # 拟合数据
    model.fit(cost, profit)

    # 预测下一年的利润
    predicted_profit = model.predict([[1200]])
    print("预测的利润：", predicted_profit[0])

    # 输出模型参数
    slope = model.coef_[0]
    intercept = model.intercept_
    print("斜率：", slope)
    print("截距：", intercept)

    # 输出线性回归模型的算式
    print("线性回归模型: y = {:.2f}x + {:.2f}".format(slope, intercept))

    # 绘图表示
    import matplotlib.pyplot as plt

    # 绘制成本和利润的数据点
    plt.scatter(cost, profit)

    # 添加线性回归模型的拟合曲线
    plt.plot(cost, model.predict(cost), color='red')

    # 显示图表
    plt.show()
