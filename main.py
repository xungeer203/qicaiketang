import pandas as pd
from functools import reduce
import pinyin_finder
import writedoc

# df = pd.read_csv("ciyu_data.csv", index_col="no", nrows=10)
df = pd.read_csv("ciyu_data.csv", index_col="no")
# print(df)
ciyus = df.ci.to_list()
ciyus = [x.split(", ") for x in ciyus]  # 词语列表
ciyus_jinsi = df.jisici_zuci.tolist()
ciyus_jinsi = [x.split(", ") for x in ciyus_jinsi]  # 近似词列表
ciyus_total = [x+y for x, y in zip(ciyus, ciyus_jinsi)]  # 词语总列表, todo: 形近字高亮

n_total = len(reduce(lambda x,y: x+y, ciyus_total))
df2 = pd.DataFrame(index=range(n_total), columns=[
    "no",
    "ci",
    "pinyin_find",
    "duoyinzi",
    "pinyin_final",
    "zi_no",
    "pianmu",
    "nianji"])  #编号, 词, 查到的拼音, 是不是多音字, 最后确定的拼音, 生字编号, 课文编号, 年级

i = 0
zi_no = 0
for yizu in ciyus_total:

    zi_no += 1
    for yige in yizu:
        pinyin_find, duoyinzi = pinyin_finder.operation(yige)

        df2.at[i,"no"] = i+1
        df2.at[i,"ci"] = yige
        df2.at[i,"pinyin_find"] = pinyin_find
        df2.at[i, "duoyinzi"] = duoyinzi
        df2.at[i, "pinyin_final"] = pinyin_find  # 暂时填充, 用查到的拼音. 后面再修改
        df2.at[i,"zi_no"] = int(zi_no)
        df2.at[i,"pianmu"] = df.at[zi_no, "pianmu"]
        df2.at[i,"nianji"] = df.at[zi_no, "nianji"]

        i += 1

# 修改多音字的错误
# todo: to be optimized
# print(df2.loc[[1160], ["ci", "pinyin_final"]])
alist = [13,136,152,385,520,583,613,627,644,713,821,848,971,981,1005,1223,1232,1237,1308,1443]
mod_list = [['qiú', '*tǐ'],['gòu', '*shù'],['shuāng', '*bì'],['yī', '*qǔ'],['mào', '*pào'],['chuí', '*dǎ'],['yī', '*zhuàng'],['dā', '*tái'],['*shā', '*lā'],['*shèng', '*huì'],['*láo', '*dao'],['yín', '*fà'],['tǎng', '*zhe'],['kào', '*zhe'],['cǎi', '*tà'],['lí', '*dì'],['gāng', 'róu', '*bìng', '*jì'],['yī', 'yáo', 'yī', '*huàng'],['liè', '*qí'],['hòu', '*bèi']]
for i, mod in zip(alist, mod_list):
    df2.at[i, "pinyin_final"] = mod

# print(df2.loc[list, "pinyin_final"])

# df2 = df2.set_index("zi_no")
# start = 1
# end = 50
# alist = list(range(start, end))
# df_today = df2.loc[alist]
# # print(df_today)
# ciyus_today = df_today.ci.tolist()
# yinyins_today = df_today.pinyin_final.tolist()
# # print(ciyus_today)
# # print(yinyins_today)
# # print("---")
# writedoc.writedoc(ciyus_today, yinyins_today)



m=5  # 每天几个字?
i=1
start = 1
zi_amount = df2["zi_no"].max()
# print(zi_amount)
df2 = df2.set_index("zi_no")
while start <= zi_amount:
    # start = (i-1)*m+1
    start = start
    end = m*i if m*i <= zi_amount else zi_amount
    alist = list(range(start, end+1))
    df_today = df2.loc[alist]
    ciyus_today = df_today.ci.tolist()
    yinyins_today = df_today.pinyin_final.tolist()
    title = "第" + str(start) + " to " "第" + str(end)
    file_name = title + ".docx"
    # print(title)
    writedoc.writedoc(ciyus_today, yinyins_today, title, file_name)

    print(f"{i}/{zi_amount/m} printed.")
    i += 1
    start = (i - 1) * m + 1







# file_name = "test.xlsx"
# df2.to_excel(file_name)


