import requests
import os
import bs4

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# MacOS 環境會檔 SSL

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}  

url = input('input link :')
# https://www.behance.net/gallery/96577587/_

response = requests.get(url,headers=headers)
# print(response.text)

print(response.status_code)
print(type(response))

# 確認連線狀態

# mkdir = input('input file directory: ')

mkdir = 'memesgeneration'

if not os.path.exists(mkdir):
    os.mkdir(mkdir)

contents = bs4.BeautifulSoup(response.text, 'lxml')

allimg = contents.select('img')
print("圖片數量:", len(allimg))

if len(allimg) > 0:
    for i in range(0, len(allimg)):
        imgurl = allimg[i].get('src')
        urllist = url.rsplit('/',1)
        finurl = urllist[0]+imgurl
        try:
            picture = requests.get(finurl)        
            picture.raise_for_status() 
            print("%s 圖片下載成功" % finurl)
            pictFile = open(os.path.join(mkdir, os.path.basename(imgurl)), 'wb')
            for diskStorage in picture.iter_content(10240):
                pictFile.write(diskStorage)
            pictFile.close()                        # 關閉檔案
        except Exception as err:
            print(f"圖片下載失敗: {err}")
