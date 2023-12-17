def Highnumberhistogram(mathScore):
    # 绘制高数直方图
    plt.suptitle("成绩分布直方图")
    plt.subplot(3, 1, 1)
    plt.hist(data.高数, bins=10, range=(0, 100), color='red')  # 0-100分,分成10段
    plt.xlabel("高数成绩分数段")  # 设置x轴标签
    plt.ylabel("人数")  # 设置y轴标签
    plt.xlim(0, 100)  # 设置x轴区间
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # 设置x轴刻度
    plt.yticks([0, 2,4,6,8,10,12,14,16,18,20])  # 设置y轴刻度
    plt.grid()#格子
    #plt.show()

def Englishhistogram(engScore):
    # 绘制英语直方图
    plt.subplot(3, 1, 2)
    plt.hist(data.大学英语, bins=10, range=(0, 100), color='blue')  # 0-100分,分成10段
    plt.xlabel("英语成绩分数段")  # 设置x轴标签
    plt.ylabel("人数")  # 设置y轴标签
    plt.xlim(0, 10)  # 设置x轴区间
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # 设置x轴刻度
    plt.yticks([0, 2,4,6,8,10,12,14,16,18,20])  # 设置y轴刻度
    plt.grid() #格子
    #plt.show()

def Scorehistogram(pythonScore):
    # 绘制python直方图
    plt.suptitle("成绩分布直方图")
    plt.subplot(3, 1, 3)
    plt.hist(data.Fython程序设计, bins=10, range=(0, 100), color='green')  # 0-100分,分成10段
    plt.xlabel("Python成绩分数段")  # 设置x轴标签
    plt.ylabel("人数")  # 设置y轴标签
    plt.xlim(0, 100)  # 设置x轴区间
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # 设置x轴刻度
    plt.yticks([0, 2,4,6,8,10,12,14,16,18,20])  # 设置y轴刻度
    plt.grid()#格子
    #plt.show()

if __name__ == '__main__':

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # 读取学生成绩数据
    # 记得改路径
    data = pd.read_csv("C:/Users/啊二/Desktop/大三复习/python/85213745/venv/第九次作业/studnt-score.csv",encoding='gbk')
    #data = pd.read_csv("C:/Users/啊二/Desktop/studnt-score.csv")

    # 计算每个学生的三门课程的总分
    total_score = data.高数 + data.大学英语 + data.Fython程序设计
    # 将total_score转换为numpy数组
    total_score = np.array(total_score)
    # 将numpy数组保存到文件中
    np.savetxt("total_score.csv", total_score, delimiter=",")
    # 读取total_score.csv文件
    total_score = np.loadtxt("total_score.csv", delimiter=",")
    print("每个学生的三门课程总分：")
    print(total_score)

    # 计算此班级每门课程的平均分和最高分及最低分
    Math_avg = data.高数.mean()
    English_avg = data.大学英语.mean()
    Python_avg = data.Fython程序设计.mean()

    Math_max = data.高数.max()
    Math_min = data.高数.min()

    English_max = data.大学英语.max()
    English_min = data.大学英语.min()

    Python_max = data.Fython程序设计.max()
    Python_min = data.Fython程序设计.min()

    print("每门课程的最高分")
    print(Math_max,English_max,Python_max)

    print("每门课程的最低分")
    print(Math_min,English_min,Python_min)

    print("每门课程的平均分")
    print(Math_avg,English_avg,Python_avg)

    #设置字体
    plt.rcParams['font.sans-serif'] =['Simhei']
    plt.rcParams['axes.unicode_minus'] = False
    # 绘制三门课程的成绩分布直方图

    # 创建一个包含三个子图的图形
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    # 调用每个子图的绘制函数
    Highnumberhistogram(data.高数)
    Englishhistogram(data.大学英语)
    Scorehistogram(data.Fython程序设计)
    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图形
    plt.show()
