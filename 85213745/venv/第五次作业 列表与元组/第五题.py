if __name__ == '__main__':
    scores = []
    for i in range(10):
        score = float(input("请输入第{}位学生的考试成绩：".format(i + 1)))
        scores.append(score)

    max_score = max(scores)
    min_score = min(scores)
    average_score = sum(scores) / len(scores)

    print("最高分：", max_score)
    print("最低分：", min_score)
    print("平均分：", average_score)