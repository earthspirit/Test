import requests
from bs4 import BeautifulSoup

url = requests.get("http://pic.yesky.com/c/6_243.shtml")
url.encoding = ('utf-8')
soup = BeautifulSoup(url.text,"html.parser")

image = soup.findAll("img")
i = 0
for src in image:
    img = requests.get(src['src'])
    if img.status_code ==200:
        open("./jpg/"+str(i)+'logo.jpg','wb').write(img.content)
        i=i+1

