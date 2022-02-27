### 網路爬蟲基礎實作(I)-Pandas模組


### Pandas

* 資料前處理的工具

---

資料結構：

* Series
索引標籤和實際值的陣列組合 

* DataFrame
base on numpy 
表格結構

pip 安裝套件

```python
import pandas as pd

stocks = pd.Series([60, 27, 72, 53], index=['a', 'b', 'c', 'd'])
print(stocks)

```

dtype: int64

int64	64 位有符號整數, numpy的資料型別

dictinary 也可轉成Series

```python



stocks pd.DataFrame(data,columns=['name','year', 'month', 'day'])


[
  {
    "日期": "2022/02/18",
    "農曆": "十八",
    "白肉雞(2.0Kg以上)": "31.5",
    "白肉雞(1.75-1.95Kg)": "31.5",
    "白肉雞(門市價高屏)": "33.0",
    "雞蛋(產地)": "36.5"
  },
  {
    "日期": "2022/02/17",
    "農曆": "十七",
    "白肉雞(2.0Kg以上)": "31.5",
    "白肉雞(1.75-1.95Kg)": "31.5",
    "白肉雞(門市價高屏)": "33.0",
    "雞蛋(產地)": "36.5"
  }
]

json 轉 diction


```


To activate this project's virtualenv, run pipenv shell.
建立建立環境變數 shell

pipenv install pandas 以此類推


YAHOO 全球：

https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0

https://finance.yahoo.com/quote/MSFT/history?p=MSFT

https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1614352901&period2=1645888901&interval=1d&events=history&includeAdjustedClose=true


https://query1.finance.yahoo.com/v7/finance/download/TSM?period1=1614433498&period2=1645969498&interval=1d&events=history&includeAdjustedClose=true


股票代號 2330 0050

證交所 TW nasdaq


1970年1月1日開始算起的秒數


台灣證交所：

ttps://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220201&stockNo=2330&_=1645885402256

20220201 2330 json




---


### link : 

[https://blog.techbridge.cc/2020/09/21/python-pandas-zen-tutorial/](https://blog.techbridge.cc/2020/09/21/python-pandas-zen-tutorial/)

[https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html](https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html)

[python：利用pandas輕鬆選股/#zi_liao_chu_li](https://www.finlab.tw/python%EF%BC%9A%E5%88%A9%E7%94%A8pandas%E8%BC%95%E9%AC%86%E9%81%B8%E8%82%A1/#zi_liao_chu_li)

https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html


外匯辭典：
https://www.oanda.com/bvi-ft/lab-education/dictionary/


