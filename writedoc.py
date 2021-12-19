import export

def writedoc(ciyus_today, pinyins_today, title, file_name):

    ciyus = ciyus_today
    pinyins = pinyins_today

    char_size = 12  # a character is 14mm width
    char_size_half = char_size * 0.2
    width_available = 145  # a single page width is 145mm

    # print(ciyus)
    # print(pinyins)

    pinyins_out = [[]]
    zis_out = [[]]
    i = 0
    n_ciyu = 0
    new_pinyins = []
    new_zis = []
    i_ciyus = 0
    # for ciyu, pinyin in zip(ciyus, pinyins):
    while i_ciyus < len(ciyus):
        # print(f"{ciyu}:{pinyin}")

        ciyu = ciyus[i_ciyus]
        pinyin = pinyins[i_ciyus]
        # print(f"{ciyu}:{pinyin}")

        if not len(zis_out):
            width_occupied = 0
        else:
            widths_zi = [char_size if x != "" else char_size_half for x in zis_out[i]]
            width_occupied = sum(widths_zi)

        # if not new_pinyins:
        for zi, zi_pinyin in zip(ciyu, pinyin):
            new_pinyins.append(zi_pinyin)
            new_zis.append(zi)



        width_new = len(new_zis) * char_size
        # print("*******")
        # print(pinyins_out)
        # print(zis_out)
        # print(new_pinyins)
        # print(new_zis)
        # print(f"{width_occupied} <> {width_available}")
        # print(f"{width_occupied+width_new} <> {width_available}")
        # print(f"{width_occupied+width_new+char_size_half} <> {width_available}")
        # print("\n")
        # print("*******")
        if (width_occupied + width_new) > width_available:
            i += 1
            n_ciyu = 0
            zis_out.append([])
            pinyins_out.append([])
            new_pinyins = []
            new_zis = []
        elif (width_occupied + width_new + char_size_half) > width_available:
            for new_zi, new_pinyin in zip(new_zis, new_pinyins):
                zis_out[i].append(new_zi)
                pinyins_out[i].append(new_pinyin)
            i += 1
            n_ciyu = 0
            zis_out.append([])
            pinyins_out.append([])
            new_pinyins = []
            new_zis = []
            i_ciyus += 1
        else:
            for new_zi, new_pinyin in zip(new_zis, new_pinyins):
                zis_out[i].append(new_zi)
                pinyins_out[i].append(new_pinyin)
            zis_out[i].append("")
            pinyins_out[i].append("")
            i_ciyus += 1
            new_pinyins = []
            new_zis = []

    # print("-----***-----")
    # print(ciyus)
    # print(pinyins)
    # for row_pinyin, row_zi in zip(pinyins_out, zis_out):
    #     print(row_pinyin)
    #     print(row_zi)
    export.export2word(pinyins_out, zis_out, char_size, char_size_half, title, file_name)
    # print("Job done.")