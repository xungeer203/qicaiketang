import pandas as pd
from functools import reduce
import pinyin_finder
import writedoc
from math import ceil

no_zi_per_day = 5  # 每页几个字?
no_zi_read = 50  # 从数据库读取几个字？ 非正数（no_zi_read <= 0）表示全部读入
my_directory = r"user\today\\"

if no_zi_read > 0:
    df_zi = pd.read_csv("ciyu_data.csv", index_col="no", nrows=no_zi_read)
else:
    df_zi = pd.read_csv("ciyu_data.csv", index_col="no")

ciyus = df_zi["ci"]
ciyus = [x.split(", ") for x in ciyus]  # 词语列表
ciyus_jinsi = df_zi["jisici_zuci"]
ciyus_jinsi = [x.split(", ") for x in ciyus_jinsi]  # 近似词列表
ciyus_total = [x+y for x, y in zip(ciyus, ciyus_jinsi)]  # 词语总列表, todo: 形近字高亮

n_total = len(reduce(lambda x,y: x+y, ciyus_total))  # 词语总数
# df_ci 是按词语展开的dataframe, 不同于df_zi是按字展开的dataframe
df_ci = pd.DataFrame(index=range(n_total), columns=[
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

        df_ci.at[i,"no"] = i+1
        df_ci.at[i,"ci"] = yige
        df_ci.at[i,"pinyin_find"] = pinyin_find
        df_ci.at[i, "duoyinzi"] = duoyinzi
        df_ci.at[i, "pinyin_final"] = pinyin_find  # 暂时填充, 用查到的拼音. 后面再修改
        df_ci.at[i,"zi_no"] = int(zi_no)
        df_ci.at[i,"pianmu"] = df_zi.at[zi_no, "pianmu"]
        df_ci.at[i,"nianji"] = df_zi.at[zi_no, "nianji"]

        i += 1

# 修改多音字的错误
# todo: to be optimized
# todo: to be modified becaue return of function pinyin_finder.operation() is changed.
# print(df_ci.loc[[1160], ["ci", "pinyin_final"]])
alist = [13,136,152,385,520,583,613,627,644,713,821,848,971,981,1005,1223,1232,1237,1308,1443]
mod_list = [['qiú', '*tǐ'],['gòu', '*shù'],['shuāng', '*bì'],['yī', '*qǔ'],['mào', '*pào'],['chuí', '*dǎ'],['yī', '*zhuàng'],['dā', '*tái'],['*shā', '*lā'],['*shèng', '*huì'],['*láo', '*dao'],['yín', '*fà'],['tǎng', '*zhe'],['kào', '*zhe'],['cǎi', '*tà'],['lí', '*dì'],['gāng', 'róu', '*bìng', '*jì'],['yī', 'yáo', 'yī', '*huàng'],['liè', '*qí'],['hòu', '*bèi']]
# for i, mod in zip(alist, mod_list):
#     df_ci.at[i, "pinyin_final"] = mod

# m=50  # 每天几个字?
i=1
start = 1
zi_amount = df_ci["zi_no"].max()
df_ci = df_ci.set_index("zi_no")
while start <= zi_amount:
    start = start
    end = no_zi_per_day*i if no_zi_per_day*i <= zi_amount else zi_amount
    alist = list(range(start, end+1))
    df_today = df_ci.loc[alist]
    ciyus_today = df_today["ci"]
    pinyins_today = df_today["pinyin_final"]
    title = f"第{str(start)}字到第{str(end)}字"
    file_name = my_directory + title + ".docx"
    writedoc.writedoc(ciyus_today, pinyins_today, title, file_name)

    print(f"{i}/{ceil(zi_amount/no_zi_per_day)} printed.")
    i += 1
    start = (i - 1) * no_zi_per_day + 1
