from pypinyin import pinyin as c_py
from pypinyin_dict.pinyin_data import kxhc1983
from pypinyin_dict.pinyin_data import ktghz2013
import export
from functools import reduce


def operation(ciyu="落下"):

    # pypinyin默认的字典，里面的多音字太多了（有可能是港澳台日韩读音）。这里采用《通用规范汉字字典》（ktghz2013）的拼音数据。
    # ref：https://pypinyin.readthedocs.io/zh_CN/master/usage.html#custom-dict （注意：这网站的代码可能过时了，有些class名字大写错了。）
    # kxhc1983.load()  # 《现代汉语词典》：这个库不准，比如“绕”不是多音字，不知道这里面的多音哪来的。
    ktghz2013.load()  # 《通用规范汉字字典》

    ciyu_pinyin_find = []
    # zi_pinyin_duo = []
    ciyu_pinyin = c_py(ciyu, heteronym=False)  # 多音字: 按词语获取拼音,可以获得更准确的拼音(相对按字查拼音).
    for zi, zi_pinyin in zip(ciyu, ciyu_pinyin):
        zi_pinyin_duo = c_py(zi, heteronym=True)[0]
        zi_pinyin_no = len(zi_pinyin_duo)
        is_duoyinzi = "n" if zi_pinyin_no == 1 else "y"
        marker_duoyinzi = "" if zi_pinyin_no == 1 else "*"

        # if is_duoyinzi == "y":
        #     # marker_duoyinzi = "*"
        #     zi_pinyin_duo = reduce(lambda x, y: x + " " + y, zi_pinyin_duo)
        #     zi_pinyin = zi_pinyin[0] + "*" + zi_pinyin_duo



        ciyu_pinyin_find.append(marker_duoyinzi + zi_pinyin[0])  # 拼音前面加星标,如果这个字是多音字.
        # ciyu_pinyin_find.append(zi_pinyin_duo)  # 拼音前面加星标,如果这个字是多音字.
        # zi_pinyin_duo.append(zi)
        # if is_duoyinzi == "y":
        #     # zi_pinyin_duo.append(zi)
        #     print(zi)
        #     for x in zi_pinyin_duo:
        #         # zi_pinyin_duo.append(x)
        #         print(x)
        #     print("-")


    return ciyu_pinyin_find, is_duoyinzi
    # return zi_pinyin_duo, is_duoyinzi