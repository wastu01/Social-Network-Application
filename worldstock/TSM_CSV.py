from io import StringIO
from tracemalloc import start
import requests
import pandas as pd
import matplotlib.pyplot as plt

	
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}  

time1=1614957713
time2=1646493713
start_time = "2022-03-04"

url = f"https://query1.finance.yahoo.com/v7/finance/download/TSM?period1={time1}&period2={time2}&interval=1d&events=history&includeAdjustedClose=true"

print(url)
# Time Period:Mar 05, 2021 - Mar 05, 2022
# v7 csv , v8 json 

# TSM 
# https://query1.finance.yahoo.com/v7/finance/download/TSM?period1=1614957713&period2=1646493713&interval=1d&events=history&includeAdjustedClose=true

response = requests.get(url,headers=headers)
# print(response.text)
print(response.status_code)
print(type(response))

# DataFrame(資料,index=時間戳)
# 去 postman 看該 資料結構
df = pd.read_csv(StringIO(response.text),index_col = "Date",parse_dates = ["Date"])

# print(df.head())

# print(df.tail(10))

# Date,Open,High,Low,Close,Adj Close,Volume

print(df.iloc[[0,3,4]])
print(df.iloc[0:4])
print()
# print(start_time)
# print(df.loc[start_time])


# df.reset_index(inplace=True)
# print(df.index)


# date = df["Date"]
# start_price = df["Open"]
# high_price = df["High"]
# low_price = df["Low"]
# end_price = df["Close"]

# # 繪圖
# plt.plot(date, high_price)
# plt.plot(date, low_price)
# plt.plot(date, end_price)

	
print(df.Close.plot(figsize=(12,5)))

# 存成圖片(一定要放前面!)
# plt.savefig("index.png")
# 顯示圖片
print(plt.show())





