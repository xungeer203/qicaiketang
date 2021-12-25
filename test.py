"""

this is temporary testing

"""

from pypinyin import pinyin as c_py
from pypinyin_dict.pinyin_data import ktghz2013
import pinyin_finder

ciyu = "朝阳"

ktghz2013.load()
ciyu_pinyin = c_py(ciyu, heteronym=True)
print(ciyu_pinyin)


pinyin_find, duoyinzi = pinyin_finder.operation(ciyu)
# print(duoyinzi)
print(pinyin_find)

print("------")
x="*"
y="zhao"
z=x+y
# test=[]
print([x+y])
# z=list(x+y)
# print(z)
print(type([x+y]))


