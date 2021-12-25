"""

try to count how many ci, zi were done.
todo: not succeeded yet.

"""


import pandas as pd
from collections import Counter
df = pd.read_csv("ciyu_data.csv", index_col="no")
print(df)

ci_group = df.ci.tolist()
# print(ci_group)
zi_get = []
count_shengzi = 0
count_ci =0
count_zi = 0

for ci_list in ci_group:
    # ci_list = df.at[1,"ci"]
    # print(ci_list)
    # print(type(ci_list))
    res = Counter(ci_list)
    res = max(res, key = res.get)
    zi_get.append(res)

    count_shengzi += 1

    for s in ci_list:
        if s.isalpha():
            count_ci += 1
        for c in s:
            if c.isalpha():
                count_zi += 1

print(zi_get)
print(count_shengzi)
print(count_zi)
print(count_ci)


df2 = pd.DataFrame(zi_get, columns=["colummn"])
df2.to_csv('zi_get.csv', index=False, encoding="utf_8_sig")
