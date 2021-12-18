from pypinyin import pinyin as c_py
import export

char_size = 11  # a character is 14mm width
# todo: "zhuang" is longer than 14mm???
char_size_half = char_size * 0.2
width_available = 145  # a single page width is 145mm

ciyus = ["落下", "荒地", "落下", "庄庄", "村庄", "洛阳", "联络", "荒野", "荒芜", "荒地", "饥荒", "荒年", "慌张", "说谎"]
# todo: "落下" 多音字 显示不出来？？？

pinyins = [[]]
zis = [[]]
i = 0
n_ciyu = 0
new_pinyins = []
new_zis = []
# width_occupied = 0
for ciyu in ciyus:
    # todo: heteronym to be added and checked.

    if not len(zis):
        # n_zi = 0
        width_occupied =0
    else:
        # n_zi = len(zis[i])
        widths_zi = [char_size if x != "" else char_size_half for x in zis[i]]
        width_occupied = sum(widths_zi)

    # width_occupied = n_zi * char_size + n_ciyu * char_size_half


    if not new_pinyins:
        for zi in ciyu:
            # print(c_py(zi, heteronym=False))

            new_pinyins.append(c_py(zi, heteronym=False)[0][0])
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

