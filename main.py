from pypinyin import pinyin as c_py
from pypinyin_dict.pinyin_data import kxhc1983
import export

# pypinyin默认的字典，里面的多音字太多了（有可能是港澳台日韩读音）。这里采用《现代汉语词典》（kxhc1983）的拼音数据。
# ref：https://pypinyin.readthedocs.io/zh_CN/master/usage.html#custom-dict
kxhc1983.load()

char_size = 11  # a character is 14mm width
char_size_half = char_size * 0.2
width_available = 145  # a single page width is 145mm

ciyus = ["落下", "荒地", "落下", "庄庄", "村庄", "洛阳", "联络", "荒野", "荒芜", "荒地", "饥荒", "荒年", "慌张", "说谎"]

pinyins = [[]]
zis = [[]]
i = 0
n_ciyu = 0
new_pinyins = []
new_zis = []
# width_occupied = 0
for ciyu in ciyus:

    if not len(zis):
        width_occupied =0
    else:
        widths_zi = [char_size if x != "" else char_size_half for x in zis[i]]
        width_occupied = sum(widths_zi)

    if not new_pinyins:
        ciyu_pinyin = c_py(ciyu, heteronym=False)  # 多音字: 按词语获取拼音,可以获得更准确的拼音(相对按字查拼音).
        for zi, zi_pinyin in zip(ciyu, ciyu_pinyin):

            zi_pinyin_no = len(c_py(zi, heteronym=True)[0])
            marker_duoyinzi = "" if zi_pinyin_no == 1 else "*"
            # print(c_py(zi, heteronym=True))
            new_pinyins.append(marker_duoyinzi+zi_pinyin[0])  # 拼音前面加星标,如果这个字是多音字.
            new_zis.append(zi)

    width_new = len(new_zis) * char_size
    # print(pinyins)
    # print(zis)
    # print(new_pinyins)
    # print(new_zis)
    # print(f"{width_occupied} <> {width_available}")
    # print(f"{width_occupied+width_new} <> {width_available}")
    # print(f"{width_occupied+width_new+char_size_half} <> {width_available}")
    # print("\n")
    if (width_occupied + width_new) > width_available:
        i += 1
        n_ciyu = 0
        zis.append([])
        pinyins.append([])
    elif (width_occupied + width_new + char_size_half) > width_available:
        for new_zi, new_pinyin in zip(new_zis, new_pinyins):
            zis[i].append(new_zi)
            pinyins[i].append(new_pinyin)
        i += 1
        n_ciyu = 0
        zis.append([])
        pinyins.append([])
    else:
        for new_zi, new_pinyin in zip(new_zis, new_pinyins):
            zis[i].append(new_zi)
            pinyins[i].append(new_pinyin)
        zis[i].append("")
        pinyins[i].append("")
        new_pinyins = []
        new_zis = []



# for pinyin in pinyins:
#     print(pinyin)
#     print("\n")
# for zi in zis:
#     print(zi)
#     print("\n")

export.export2word(pinyins, zis, char_size, char_size_half)

print("Job done.")

