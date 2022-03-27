import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8,'font.sans-serif':'Taipei Sans TC Beta'})
# 全域字體設定


df = pd.read_csv("./2330_month_stock.csv",index_col="日期", encoding="UTF-8")
# df.index = pd.to_datetime(df.index)
#  將日期指定為索引

date = df.index 
open_price = df["開盤價"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

# 查看前五筆 後五筆
print(df.head())
print(df.tail())

plt.figure(figsize=(12,8))
# plt.plot(date,open_price,'-', color="#089950", label="開盤價")
plt.plot(date,high_price,'-', color="#089950", label="最高價",linewidth=6,marker="*")
plt.plot(date,low_price, '-', color="#00bd42", label="最低價",linewidth=5)
plt.plot(date,end_price,'--', color="#f23645", label="收盤價",linewidth=1, marker=".")
plt.xlabel("日期",fontsize=20)
plt.ylabel("價格",fontsize=20)
plt.legend(["最高價", "最低價", "收盤價"], loc="lower right",shadow=True)
plt.title("111年2月台股台積電趨勢圖")
plt.grid(True, axis='y')

# 存成圖片(一定要放前面!)
plt.savefig("111年2月台股台積電趨勢圖.png")
# 顯示圖片
plt.show()
