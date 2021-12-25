import export

def writedoc(ciyus_today, pinyins_today, title, file_name):

    ciyus = ciyus_today  # pandas series　数据类型
    ci_pinyins = pinyins_today  # pandas series　数据类型

    char_size = 12  # 一个字的宽度
    spacer = char_size * 0.2  # 词间隔：词和词之间的间距
    width_available = 145  # 一行的宽度

    pinyins_out = [[]]  # 最终输出到word的拼音矩阵: [[第一行],[第二行],[第三行], ..., [最后一行]]
    zis_out = [[]]  # 最终输出到word的单字矩阵: [[第一行],[第二行],[第三行], ..., [最后一行]]
    i = 0  # pinyins_out 的行数指针:　i=0>第一行，　i=1>第二行，　i=2>第三行，　...
    # n_ciyu = 0
    new_pinyins = []  # 可能被添加到pinyins_out某一行的词语, 最终是否添加,取决于加入改词语后,这一行会不会超宽
    new_zis = []
    i_ciyus = 0  # 指针：用来便利ciyus里面的词语

    # 遍历所有词语
    # 一个词语会被添加到inyins_out某一行的词语, 最终是否添加,取决于加入改词语后,这一行会不会超宽了
    while i_ciyus < len(ciyus):

        ciyu = ciyus.iloc[i_ciyus]  # 取出一个词
        ci_pinyin = ci_pinyins.iloc[i_ciyus]

        # 当前行已经被占领了的宽度：
        if not len(zis_out):
            width_occupied = 0  # 当前行已经被占用了width_occupied宽度, 如果当前行一个字都没有,width_occupied=0
        else:
            widths_zi = [char_size if x != "" else spacer for x in zis_out[i]]
            width_occupied = sum(widths_zi)  # 当前行已经被占用了width_occupied宽度

        # 把取出的词放到new_pinyins列表里
        for zi, zi_pinyin in zip(ciyu, ci_pinyin):  # 因为pinyin = [[zhao],[yang]]，zi_pinyin是list，
            new_pinyins.append(zi_pinyin[0])  # 所以这里要用zi_pinyin[0]
            new_zis.append(zi)


        # 新词需要占领的宽度：
        width_new = len(new_zis) * char_size

        # 如果当前行加入新词，是否会超出行宽度：
        if (width_occupied + width_new) > width_available:  # 只增加新词会超宽吗
            i += 1  # 行指针
            # n_ciyu = 0  #
            zis_out.append([])  # 新增一行：空行
            pinyins_out.append([])  # 新增一行：空行
            new_pinyins = []  # 清空new_pinyins
            new_zis = []  #
        elif (width_occupied + width_new + spacer) > width_available:  # 增加新词以及词间隔会超宽吗
            # 把新词添加到当前行，但是不添加词间隔
            for new_zi, new_pinyin in zip(new_zis, new_pinyins):
                zis_out[i].append(new_zi)
                pinyins_out[i].append(new_pinyin)
            i += 1  # 行指针
            # n_ciyu = 0
            zis_out.append([])  # 新增一行：空行
            pinyins_out.append([])  # 新增一行：空行
            new_pinyins = []  # 清空new_pinyins
            new_zis = []
            i_ciyus += 1  # 指针指向下一个词
        else:  # 不会超宽：增加新词以及词间隔会超宽
            # 把新词添加到当前行，但是不添加词间隔
            for new_zi, new_pinyin in zip(new_zis, new_pinyins):
                zis_out[i].append(new_zi)
                pinyins_out[i].append(new_pinyin)
            zis_out[i].append("")  # 添加词间距
            pinyins_out[i].append("")
            i_ciyus += 1  # 指针指向下一个词
            new_pinyins = []  # 清空new_pinyins
            new_zis = []

    export.export2word(pinyins_out, zis_out, char_size, spacer, title, file_name)
