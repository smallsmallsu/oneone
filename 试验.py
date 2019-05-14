import requests
from bs4 import BeautifulSoup
import re
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
fzuhrefs=[]
for fzui in range(1,5):
    url="https://news.fzu.edu.cn/html/fdyw/"+str(fzui)+".html"
    r=requests.get(url,headers=headers,timeout=10)
    soup=BeautifulSoup(r.text,"r.text.parser")
    allhrefs=soup.find_all("div",class_="list_main_content")
    for allhref in allhrefs:
        fzuhrefs=allhref.find_all("a")
        for fzuhref in fzuhrefs:
            print(fzuhref.get_text())
