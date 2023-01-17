# beautifulsoup4

套件安裝：[https://pypi.org/project/beautifulsoup4/](https://pypi.org/project/beautifulsoup4/)

目的：key in 網址 設定 mkdir 解析網址儲存 all of img


選定的是系上線上展覽網址：[學生聯展作品](https://memesgeneration.weebly.com/23416299833287923637.html)

## 第一步 創立虛擬環境，避免污染環境

pipenv --three
pipenv run / pipenv shell

## 第二步 安裝 beautifulsoup4 , request , ssl (macos 環境才需要)

pipenv install xxx

```python=
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# MacOS 環境會檔 SSL
# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
```

## 第三步 先把 requests get 到的 url 確認狀態是否正常

```python=
print(response.status_code)
print(type(response))
# 確認連線狀態
```

## 第四步 指定存放位置資料夾

mkdir 也是終端機常用命令

```python=
os.mkdir(mkdir)
```

## 第五步 解析網址

```python=
contents = bs4.BeautifulSoup(response.text, 'lxml')

print("圖片數量:", len(allimg))
```

> lxml 是什麼？ beautifulsoup4其中之一解析器，速度較快
> len 是什麼？是計算 string, list ,tuple 的長度

要解析的圖片網址需要處理該怎麼辦？

語法：str.split(str='分隔的符號', (分割次數)).

url = url.split('/ ', 1 );  
#以斜線為分割，從『前面』數來分隔一次

原始 URL :
<https://wastu01.github.io/Javascript-LocalStorage>

輸出：['https:', '/wastu01.github.io/Javascript-LocalStorage']

語法：str.rsplit(str='分隔的符號',  (分割次數))
r 應該是指 reverse 的意思？

url = url.rsplit('/',1); 
#以斜線為分割，從『後面』數來分隔一次

## 實際案例

網域：[https://memesgeneration.weebly.com](https://memesgeneration.weebly.com)

子頁：[https://memesgeneration.weebly.com/23416299833287923637.html](https://memesgeneration.weebly.com/23416299833287923637.html)

子頁圖的網址：https://memesgeneration.weebly.com/uploads/1/2/9/6/129673037/adtxxx-jpg_orig.jpg

src = /uploads/1/2/9/6/129673037/adtxxx-jpg_orig.jpg

```python
allimg = contents.select('img')
imgurl = allimg[i].get('src')
urllist = url.rsplit('/',1)
realurl = urllist[0]+imgurl
```

### 參考資料

[https://ithelp.ithome.com.tw/articles/10218119](https://ithelp.ithome.com.tw/articles/10218119)

[https://www.runoob.com/python/att-string-len.html](https://www.runoob.com/python/att-string-len.html)

[https://www.runoob.com/python/att-string-split.html](https://www.runoob.com/python/att-string-split.html)

#### [Social-Network-Application 課程筆記線上檔案](https://github.com/wastu01/Social-Network-Application)
