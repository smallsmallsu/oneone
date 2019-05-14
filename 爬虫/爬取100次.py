import requests as re
import time as t
def gethtmltext(url):
    try:
        r=re.get(url,timeout=30)
        r.raise_for_status()  
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '产生异常'
    
if __name__=='__main__':
    url='https://www.baidu.com'
    start=t.perf_counter()
    for i in range(100):
        gethtmltext(url)
    end=t.perf_counter()-start
    print('爬取100次百度首页的时间：{:.3f}秒'.format(end))






















import requests as re
import time as t
def gethtmltxt(url):
    try:
         r=re.get(url,timeout=30)
         r.raise_for_status()
         r.encoding=r.apparent_encoding
         return r.text
    except:
          return 产生异常
if __name__=='__main__':
    url='https://www.baidu.com'
    start=t.perf_counter()
    for i in range(100):
        gethtmltxt(url)
    end=t.perf_counter-start
    print('爬取100次时间:{:.3f}秒'.format(end))



