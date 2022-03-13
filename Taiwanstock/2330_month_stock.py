import requests
import json
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}  

time1=20220201
# time2=20220230
stock=2330
# market="TW"
encoding ='utf-8'

url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={time1}&stockNo={stock}"

print(url)
response = requests.get(url,headers= headers)
json_data = json.loads(response.text)
print(response.status_code)
print(type(response))
datas = json_data["data"]
fields = json_data["fields"]

# 存成Pandas的Dataframe
df = pd.DataFrame(datas, columns=fields)
print(df)

# 轉成csv檔
df.to_csv("2330_month_stock.csv", encoding= encoding)
# 轉成xlsx檔
df.to_excel("2330_month_stock.xlsx", encoding= encoding)
# 轉成html檔
df.to_html("2330_month_stock.html")