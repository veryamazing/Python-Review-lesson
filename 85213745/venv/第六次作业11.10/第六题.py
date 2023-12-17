#两个字典的合并
if __name__ == '__main__':
    dicAreas = {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1,'America':936.4,
                'Brazil':854.7}
    dicCapitals = {'Russia': '莫斯科','Canada': '渥太华','China': '北京','America':'华盛顿'
        ,'Brazil':'巴西利亚'}
    dicAll = {}
    for country, capital in dicCapitals.items():
        dicAll[country] = {'area': dicAreas[country], 'capital': capital}

        dicAll = {country: {'area': dicAreas[country], 'capital': dicCapitals[country]} for country in dicCapitals}

    import pprint

    pprint.pprint(dicAll)
#使用了一个循环来遍历dicCapitals字典中的键值对，
# 并将每个国家和首都分别作为一个字典的值添加到dicAll字典中。
# 注意，我们在添加字典时，使用了国家作为字典的键，以便在后续使用时更方便地访问国家的信息。