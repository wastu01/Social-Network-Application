from io import StringIO
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime
	
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
}
while True:
    try:

        days = 86400
        stock_id = input("輸入股票代碼 : ")
        time_start = input("輸入開始日期 : ")
        time_end = input("輸入結束日期 : ")
        initial = datetime.datetime.strptime( '1970-01-01' , '%Y-%m-%d' )
        starts = datetime.datetime.strptime( str(time_start) , '%Y-%m-%d' )
        end = datetime.datetime.strptime( str(time_end), '%Y-%m-%d' )
        period1 = starts - initial
        period2 = end - initial
        s1 = period1.days * days
        s2 = period2.days * days
        print("開始時間差距 : " + str(s1))
        print("結束時間差距 : " + str(s2))
        
        url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=" + str(s1) + "&period2=" + str(s2) + "&interval=1d&events=history&includeAdjustedClose=true"
        response = requests.get(url,headers= headers)
        print(url)
        df = pd.read_csv(StringIO(response.text),index_col = "Date",parse_dates = ["Date"])
        # df.Close.plot(figsize=(12,5))
        date = df.index 
        open_price = df["Open"]
        high_price = df["High"]
        low_price = df["Low"]
        end_price = df["Adj Close"]
        print(df.head())
        
        
        plt.figure(figsize=(12,8))
        # plt.plot(date,open_price,'-', color="#089950", label="開盤價")
        plt.plot(date,high_price,'-', color="#089950", label="最高價",linewidth=6,marker="*")
        plt.plot(date,low_price, '-', color="#00bd42", label="最低價",linewidth=5)
        plt.plot(date,end_price,'--', color="#f23645", label="收盤價",linewidth=1, marker=".")
        plt.xlabel("日期",fontsize=20)
        plt.ylabel("價格",fontsize=20)
        plt.legend(["最高價", "最低價", "收盤價"], loc="lower right",shadow=True)
        plt.title(stock_id+" 趨勢圖")
        plt.grid(True, axis='y')
        
        address = "./" + stock_id + "_" + time_start + "_" + time_end + ".csv"
        df.to_csv(address)
        plt.savefig(stock_id +  "_" + time_start + "_" + time_end + "趨勢圖.png")
        # 存檔要放在 show 之前
        plt.show()
        break

    except:
        print("輸入錯誤格式，請重新輸入")
        