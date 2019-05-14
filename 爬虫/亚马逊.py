import requests
url="https://www.amazon.cn/dp/B07MTCTPQY/ref=lp_143359071_1_1?s=digital-text&ie=UTF8&qid=1555252431&sr=1-1"
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
