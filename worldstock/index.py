import json
import numpy
import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}  

time1=1614957713
time2=1646493713

url = f"https://query1.finance.yahoo.com/v8/finance/chart/TSM?period1={time1}&period2={time2}&interval=1d&events=history&=hP2rOschxO0"


# Time Period:Mar 05, 2021 - Mar 05, 2022
# v7 csv , v8 json 

# TSM 
# https://query1.finance.yahoo.com/v7/finance/download/TSM?period1=1614957713&period2=1646493713&interval=1d&events=history&includeAdjustedClose=true

response = requests.get(url,headers=headers)
data = json.loads(response.text)
# print(response.text)
print(response.status_code)
print(type(response))

# DataFrame(資料,index=時間戳)
# 去 postman 看該 json 資料結構
df = pd.DataFrame(data["chart"]["result"][0]["indicators"]["quote"][0],index=pd.to_datetime(
        numpy.array(data["chart"]["result"][0]["timestamp"]) * 1000 * 1000 * 1000))

print(df.head())





