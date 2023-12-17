if __name__ == '__main__':
    ieee_languages = ["Python", "C++", "C", "Java", "C#"]
    tiobe_languages = ["Java", "C", "Python", "C++", "VB.NET"]

    # (1) 上榜的所有语言
    all_languages = set(ieee_languages + tiobe_languages)
    print("上榜的所有语言：", all_languages)

    # (2) 在两个榜单中同时排名前五的语言
    common_languages = set(ieee_languages[:5]) & set(tiobe_languages[:5])
    print("在两个榜单中同时排名前五的语言：", common_languages)

    # (3) 只在IEEE 榜排名前五的语言
    ieee_only_languages = set(ieee_languages[:5]) - set(tiobe_languages[:5])
    print("只在IEEE 榜排名前五的语言：", ieee_only_languages)

    # (4) 只在一个榜单排名前五的语言
    only_languages = set(tiobe_languages[:5]) - set(ieee_languages[:5])\
                     | set(ieee_only_languages)
    print("只在一个榜单排名前五的语言：", only_languages)
