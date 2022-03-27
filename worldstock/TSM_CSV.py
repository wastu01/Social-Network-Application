from io import StringIO
from tracemalloc import start
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime
	
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}

while True:
    try:
        days = 24 * 60 * 60
        stock_id = input("輸入股票代碼 : ",)
        time_start = input("輸入開始日期 : ")
        time_end = input("輸入結束日期 : ")
        initial = datetime.datetime.strptime( '1970-01-01' , '%Y-%m-%d' )
        start = datetime.datetime.strptime( str(time_start) , '%Y-%m-%d' )
        end = datetime.datetime.strptime( str(time_end), '%Y-%m-%d' )
        period1 = start - initial
        period2 = end - initial
        s1 = period1.days * days
        s2 = period2.days * days

        url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=" + str(s1) + "&amp;period2=" + str(s2) + "&amp;interval=1d&amp;events=history&amp;includeAdjustedClose=true"
        print(url)
        response = requests.get(url)
        df = pd.read_csv(StringIO(response.text),index_col = "Date",parse_dates = ["Date"])
        df.Close.plot(figsize=(12,5))


        
        # Time Period:Mar 05, 2021 - Mar 05, 2022
        # v7 是 csv , v8 是 json 


        response = requests.get(url,headers=headers)
        # print(response.text)
        # print(type(response))   
        print(response.status_code) 
        # 確認連線狀況


        # DataFrame(資料,index=時間戳)
        # 去 postman 看 API 資料結構
        df = pd.read_csv(StringIO(response.text),index_col = "Date",parse_dates = ["Date"])

        # print(df.head())

        # print(df.tail(10))

        # Date,Open,High,Low,Adj Close,Volume

        # print(df.iloc[[0,3,4]]) 
        # 調出第幾筆
        print(df.iloc[0:8])
        # 第幾筆區間


        print(df.Close.plot(figsize=(12,5)))

        # 存成圖片
        # plt.savefig("收盤價.png")
        # 顯示圖片
        # print(plt.show())
        break
    except:
        print("輸入錯誤格式，請重新輸入")
address = "./" + stock_id + ".csv"
df.to_csv(address)