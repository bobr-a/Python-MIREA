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
    lst_none.clear()
    for i in range(0, len(rows)):
        lst_none.append(None)
    lst_of_col = list(zip(*rows))
    for col in lst_of_col:
        if (col not in res_lsts) and (col != tuple(lst_none)):
            res_lsts.append(col)
    res_lsts = list(map(list, zip(*res_lsts)))
    for row in res_lsts:
        if row[0] == '1':
            row[0] = 'true'
        elif row[0] == '0':
            row[0] = 'false'
        row[2] = row[2].replace('[at]', '@')
        row[1] = '(' + row[1][2:5] + ') ' + row[1][5:8] + '-' + row[1][8:]
        tmp = row[3].split('.')
        tmp.reverse()
        row[3] = "-".join(tmp)
    res = list(map(list, list(zip(*res_lsts))))
    return res


print(f23([[None, None, None, None, None, None, None],
           ['1', '+77538579641',None, 'rerov13[at]rambler.ru', '25.05.1999', None, 'rerov13[at]rambler.ru'],
           [None, None, None, None, None, None, None],
           ['1', '+72776940120',None, 'kagberg5[at]rambler.ru', '23.01.2000', None, 'kagberg5[at]rambler.ru'],
           ['1', '+74897225072', None, 'gibberg35[at]mail.ru', '02.07.1999', None, 'gibberg35[at]mail.ru'],
           ['0', '+71686315819',None, 'rizev47[at]mail.ru', '07.11.1999', None, 'rizev47[at]mail.ru']]))
