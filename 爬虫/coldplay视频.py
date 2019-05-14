import requests
import os
url="https://s1.hdslb.com/bfs/static/jinkela/video/stardust-video.0533d7d72da54ade446ecc8991b9f3f7b06575aa.js"
root="E://pics//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")

    
