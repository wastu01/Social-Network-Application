
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

year_df = pd.DataFrame()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}  

for m in range(1, 13):
    url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021{0:02d}01&stockNo=2330".format(m)
    print(url)

    response = requests.get(url, headers=headers)

    json_data = json.loads(response.text)
    datas = json_data["data"]
    fields = json_data["fields"]

    month_df = pd.DataFrame(datas, columns=fields)

    year_df = pd.concat([year_df,month_df], axis=0,join='outer',ignore_index=None)
    # outer 空的資料會用 NaN 代替，ignore_index = true 合併會自動產生新的序列 axis=0 直向合併

year_df.set_index("日期",inplace=True)

print(year_df.tail(10))
# 末項十筆

encoding ='utf-8'


year_df.to_csv("./2330_year_stock.csv", encoding= encoding)

year_df.to_excel("./2330_year_stock.xlsx", encoding= encoding)

year_df.to_html("./2330_year_stock.html")
