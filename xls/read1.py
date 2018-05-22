import xlrd

wk = xlrd.open_workbook(u'd:\公卫业务系统对比.xlsx')

shname= wk.sheet_names()
for sh in shname:
    sheet2= wk.sheet_by_name(sh)
    nrows, ncols = sheet2.nrows, sheet2.ncols
    print(nrows, ncols)
    for i in range(nrows):
        row = sheet2.row_values(i)
        for k in range(ncols):
            print( row[k])