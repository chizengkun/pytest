import tushare as ts
import datetime
#import pandas as pd
import matplotlib.pyplot as plt
import tqdm



def get_stocks_codes():
    '''
    取所有的股票代码
    :return: Index, 股票代码索引
    '''
    basics = ts.get_stock_basics()
    return basics.index

def get_stock_ma5(code, sday, delta=1):
    '''
    返回最后的收盘价 , 超过30天获取不到，不再读取对应的股票值
    :param code: 股票代码
    :param sday: 日期类型，日期
    :param delta: 增量，默认是1 向后，-1减一天
    :return: 5天的平均价ma5
    '''
    retval = 0.0
    icount = 1
    while True:
        s = sday.strftime('%Y-%m-%d')
        #print(s)
        sdata = ts.get_hist_data(code, start=s, end=s)
        if icount> 7:
            break
        if sdata is None or sdata.empty:
            sday = sday + datetime.timedelta(days= delta)
            icount += 1
            continue
        #print(sdata)
        #print(sdata.iloc[0])
        retval = sdata.iloc[0]['ma5']
        break
    return retval

def get_double_raise(indexcodes):
    '''
    获取成长性超过2倍的股票 从 2017-01-01 到 今天为止
    :param indexcodes:
    :return:
    '''
    sday = datetime.date(2017,1,1)
    eday = datetime.date.today()
    ilen = len(indexcodes)
    ret = []
    #文本进度条提醒
    for i in tqdm.trange(ilen):
        code = indexcodes[i]
        startval = get_stock_ma5(code, sday)
        endval   = get_stock_ma5(code, eday, -1)
        if endval >= startval*2:
            ret.append(code)
    return ret

def show_stocks(stocks):
    '''
    显示股票对应的价格变化曲线 -每页显示5条记录
    :return:
    '''
    print( stocks)

def main():
    codes = get_stocks_codes()
    stocks = get_double_raise(codes)
    show_stocks( stocks)

if __name__ == '__main__':
    main()