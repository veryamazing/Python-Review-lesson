#按照国家名的升序输出Russia，Canada，China三个国家和对应的国土面积。
if __name__ == '__main__':
    dicAreas={'Russia':1707.5,'Canada': 997.1,'China':960.1}
    ls = sorted(dicAreas)
    #按照国家名升序
    # for country in ls:
    #     print(country,dicAreas[country])
    #按照国土面积升序输出
    ls = sorted(dicAreas.items(),key=lambda x:x[1],reverse=False)
    for country,area in ls:
        print(country,area)