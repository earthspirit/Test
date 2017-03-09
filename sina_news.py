from bs4 import BeautifulSoup
import requests

html = requests.get('http://news.sina.com.cn/china/')
html.encoding=('utf-8')
soup = BeautifulSoup(html.text,'html.parser')
news_item = soup.select('.news-item')

# create a file to save html
f = open('f.txt','w')

for news in news_item:
    if len(news.select('h2'))>0:
        print(news.select('h2')[0].text)
        f.write(news.select('h2')[0].text)
        f.write('\n')

f.close()
