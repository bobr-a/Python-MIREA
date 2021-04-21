def f23(x):
    rows = []
    res = []
    lst_none = []
    for i in range(0, len(x[0])):
        lst_none.append(None)
    for row in x:
        if (row not in rows) and (row != lst_none):
            rows.append(row)

    res_lsts = []
    lst_of_col = list(zip(*rows))
    for col in lst_of_col:
        if col not in res_lsts:
            res_lsts.append(col)
    res_lsts = list(map(list, zip(*res_lsts)))

    for row in res_lsts:
        if row[0][0] == 'Y':
            row.insert(1, 'да')
        elif row[0][0] == 'N':
            row.insert(1, 'нет')

        row[2] = row[2].split(',')[0]
        row[0] = row[0].split('&')[1]
        row[0] = row[0].split('@')[0]


    arr = sorted([i[0] for i in res_lsts])
    i = 0
    y = 0
    while len(res) != len(res_lsts):
        if i >= len(res_lsts):
            i = 0
        if res_lsts[i][0] == arr[y]:
            res.append(res_lsts[i])
            y += 1
        i += 1

    res = list(map(list, list(zip(*res))))

    return res
