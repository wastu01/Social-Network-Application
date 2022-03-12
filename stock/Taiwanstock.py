
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

    year_df = year_df.append(month_df, ignore_index=True)

print(year_df)
year_df.to_csv("./year_stock.csv", encoding="UTF-8")
# FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.