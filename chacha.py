"""

this is only for temporary testing.

"""


from pypinyin import pinyin as c_py
from pypinyin_dict.pinyin_data import kxhc1983
from pypinyin_dict.pinyin_data import ktghz2013
import export
from functools import reduce




# pypinyin默认的字典，里面的多音字太多了（有可能是港澳台日韩读音）。这里采用《通用规范汉字字典》（ktghz2013）的拼音数据。
# ref：https://pypinyin.readthedocs.io/zh_CN/master/usage.html#custom-dict （注意：这网站的代码可能过时了，有些class名字大写错了。）
# kxhc1983.load()  # 《现代汉语词典》：这个库不准，比如“绕”不是多音字，不知道这里面的多音哪来的。
ktghz2013.load()  # 《通用规范汉字字典》

ciyu = "艳艳丽"
ciyu_pinyin_find = []
ciyu_pinyin = c_py(ciyu, heteronym=False)  # 多音字: 按词语获取拼音,可以获得更准确的拼音(相对按字查拼音).
print(ciyu_pinyin)
for zi, zi_pinyin in zip(ciyu, ciyu_pinyin):
    yin = c_py(zi, heteronym=True)[0]
    print(type(yin))
    yin = reduce(lambda x,y: x+y, yin)
    zi_pinyin_no = len(yin)
    print(type(yin))
    print(f">>{yin}")


list = [13,136,152,385,520,583,613,627,644,713,821,848,971,981,1005,1160,1223,1232,1237,1308,1443]
# mod_list = ["tǐ","shù","bì","qǔ","pào","dǎ","zhuàng","shèng","lā","tǐ","tǐ","tǐ","tǐ","tǐ","tǐ","tǐ","tǐ","tǐ","tǐ","tǐ","tǐ",]
mod_list = [['qiú', '*tǐ'],['gòu', '*shù'],['shuāng', '*bì'],['yī', '*qǔ'],['mào', '*pào'],['chuí', '*dǎ'],['yī', '*zhuàng'],['dā', '*tái'],['*shā', '*lā'],['*shèng', '*huì'],['*láo', '*dao'],['yín', '*fà'],['tǎng', '*zhe'],['kào', '*zhe'],['cǎi', '*tà'],['dī', '*dā'],['lí', '*dì'],['gāng', 'róu', '*bìng', '*jì'],['yī', 'yáo', 'yī', '*huàng'],['liè', '*qí'],['hòu', '*bèi']]

for x, y in zip(list, mod_list):
    print(f"{x}:{y}")

ciyu = '地震'
ciyu_pinyin = c_py(ciyu, heteronym=False)
print(ciyu_pinyin)