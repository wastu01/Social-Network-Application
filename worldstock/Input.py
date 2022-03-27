	
import datetime

time_start = input("輸入開始日期 : ")
time_end = input("輸入結束日期 : ")
initial = datetime.datetime.strptime( '1970-01-01' , '%Y-%m-%d' )
start = datetime.datetime.strptime( str(time_start) , '%Y-%m-%d' )
end = datetime.datetime.strptime( str(time_end), '%Y-%m-%d' )
print("初始時間 : " + str(initial))
# print("開始時間 : " + str(start))
# print("結束時間 : " + str(end))


period1 = start - initial
period2 = end - initial
# print("開始時間差距 : " + str(period1))
# print("結束時間差距 : " + str(period2))


days = 24 * 60 * 60    #一天有86400秒 
s1 = period1.days * days
s2 = period2.days * days
print("開始時間 : " + str(s1))
print("結束時間 : " + str(s2))