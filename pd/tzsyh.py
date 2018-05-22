import tushare as ts
import datetime
import pandas as pd
import os
#import numpy as np
import matplotlib.pyplot as plt
import tqdm

stockfile = u'vipstocks.npy'
stockdic = {}

def get_stocks_codes():
    '''
    取所有的股票代码
    :return: Index, 股票代码索引
    '''
    basics = ts.get_stock_basics()
    for index, row in basics.iterrows():
        stockdic[index] = row['name']
    return basics.index.values

def get_stock(code, start, end):
    return ts.get_hist_data(code, start=start, end=end)

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

def get_double_raise(valcodes):
    '''
    获取成长性超过2倍的股票 从 2017-01-01 到 今天为止
    :param indexcodes:
    :return:
    '''
    if os.path.isfile(stockfile):
        ret = pd.read_csv(stockfile)
    else:
        sday = datetime.date(2017,1,2)
        eday = datetime.date.today()
        ilen = len(valcodes)
        ret = pd.DataFrame(columns=['code','sval','eval'])
        #ret['code'] = ret['code'].astype('string')
        #文本进度条提醒
        for i in tqdm.trange(ilen):
            code = valcodes[i]
            startval = get_stock_ma5(code, sday)
            endval   = get_stock_ma5(code, eday, -1)
            #如果为 0 了就是存在问题的
            if startval>0 and endval>0 and endval >= startval*2:
                ret.loc[ret.shape[0]] = [code, startval, endval]
    if ret.shape[0]>0:
        ret.to_csv(stockfile)
    return ret

def show_stocks(stocks, stockcount=5):
    '''
    显示股票对应的价格变化曲线 -每页显示5条记录
    :return:
    '''
    # DataFrame排序，最大的5个股票
    stocks['diff'] = stocks['eval'] - stocks['sval']
    showdatas = stocks.sort_values(by='diff', ascending=False)[['code','sval','eval','diff']]
    codes = []
    for _, row in showdatas.iterrows():
        codes.append( str(int( row['code'])).zfill(6))
    #print( showdatas)
    #获取5个股票的所有对应值

    for code in codes:
        pf = get_stock(  code, datetime.date(2017,1,2).strftime('%Y-%m-%d'), datetime.date.today().strftime('%Y-%m-%d'))
        vf = pf[['close', 'ma5']]
        vf['code'] = 'A股'+code
        showFrame = pd.DataFrame(columns=['code', 'close', 'ma5']);
        showFrame = showFrame.append( vf)
        showFrame.sort_index(ascending=False)
        showFrame.plot(use_index=True, title= code +'--'+ stockdic.get(code))

        plt.show()

    #showFrame['close'] =showFrame['close'].astype('float')
    #showFrame['ma5'] = showFrame['ma5'].astype('float')
    #print(showFrame)
    #

def main():
    codes = get_stocks_codes()
    stocks = get_double_raise(codes)

    show_stocks( stocks)

if __name__ == '__main__':
    main()