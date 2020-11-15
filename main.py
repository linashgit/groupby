import pandas
import numpy
import os

if __name__ == '__main__':
    print('go')
    
    # 取得資料位置
    wdpath = os.getcwd()
    datapath = os.path.join(wdpath, '讀取的csv檔名')
    
    # 讀取csv資料
    alldata = pandas.read_csv(datapath)
    alldata['年月日的那欄'] = pandas.to_datetime(alldata['年月日的那欄'])
    
    # 分類
    sector = alldata.groupby(['契約簡稱那欄', '年月日的那欄'])
    df = sector['成交數量那欄'].mean()
    levels = df.index.levels[0] #選擇顧客指定的契約
    
    # 抽取
    A = dict()
    for i in levels:
        try:
            data = df.loc[i]['指定要的日期']
            A[i] = data
            
        except:
            pass
        
    # 轉置
    A = pandas.DataFrame([A]).T
    A.columns = ['平均交易量']
    
    # 輸出
    Apath = os.path.join(wdpath, 'A.csv')
    A.to_csv(Apath)
    