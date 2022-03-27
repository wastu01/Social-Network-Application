import requests
import json
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}  

time1=20220201
# time2=20220230 設定查詢日期參數
stock=2330
# market="TW"  台灣證券交易所個股單日成交

url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={time1}&stockNo={stock}"

print(url)
response = requests.get(url,headers= headers)
json_data = json.loads(response.text)
print(response.status_code)
# 確認連線狀況

datas = json_data["data"]
fields = json_data["fields"]

# 存成Pandas的Dataframe (列，欄)
df = pd.DataFrame(datas, columns=fields)

# 列出欄位資料型別
print(df.info())

print(df.columns)
print(df.index)

# Index(['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數'], dtype='object')
# RangeIndex(start=0, stop=15, step=1)

# 列出統計資訊 
print(df.describe())

#    count：數量統計
#    unique：唯一值數量
#    std：標準差
#    top：最常出現數值
#    freq：最常出現次數
#    因都只出現一次所以會任一選擇


df.set_index("日期",inplace=True)

print(df.tail(10))
# 末項十筆

encoding ='utf-8'

# 轉成csv檔
df.to_csv("./2330_month_stock.csv", encoding= encoding)
# 轉成xlsx檔
df.to_excel("./2330_month_stock.xlsx", encoding= encoding)
# 轉成html檔
df.to_html("./2330_month_stock.html")