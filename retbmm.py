# -*- coding: utf-8 -*-
#开发团队
#开发人员
import os
import time
import urllib ,urllib.request

from bs4 import BeautifulSoup


class ReTbmm():
    def Retbmm(self):
        start = time.time()
        self.cdir = os.getcwd()
        #爬取的网址 https://car.autohome.com.cn/pic/series/703.html#pvareaid=3454438
        #车身外观
        url1 ='https://car.autohome.com.cn/pic/series/703-1.html#pvareaid=2042222'
        #中控方向盘
        url2 = 'https://car.autohome.com.cn/pic/series/703-10.html#pvareaid=2042222'
        #车厢座椅
        url3 = 'https://car.autohome.com.cn/pic/series/703-3.html#pvareaid=2042222'
        #其他细节
        url4 = 'https://car.autohome.com.cn/pic/series/703-12.html#pvareaid=2042222'
        self.getImg('车身外观',url1)
        self.getImg('中控方向盘', url2)
        self.getImg('车厢座椅', url3)
        self.getImg('其他细节', url4)
        end =time.time()
        print("run time:" +str(end-start))

    def getImg(self,name,urls):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
        headers = {'User-Agent': user_agent}
        #访问连接
        request = urllib.request.Request(urls, headers = headers)
        #获取数据
        response = urllib.request.urlopen(request)
        #解析数据
        bsObj = BeautifulSoup(response,'html.parser')
        #查找所有img标记
        t1 = bsObj.find_all('img')
        for t2 in t1:
            t3 = t2.get('src')
            print(t3)
        #创建图片路径
        path = self.cdir+'/mrsoft/' + str(name)
        #读取路径
        if not os.path.exists(path):
            #根据路径建立图片文件夹
            os.makedirs(path)
        n = 0
        #循环图片集合
        for img in t1:
            #每次图片顺序加1
            n = n +1
            link = img.get('src')
            #判断图片路径是否存在
            if link:
                #拼接图片链接
                s = "http:" + str(link)
                #分离文件扩展名
                i= link[link.rfind('.'):]
                try:
                    #访问图片链接
                    request = urllib.request.Request(s)
                    #获取返回事件
                    response =urllib.request.urlopen(request)
                    #读取返回内容
                    imgData = response.read()
                    #创建文件
                    pathfile = path + r'/' + str(n) + i
                    #打开文件
                    with open(pathfile,'wb') as f:
                        #图片写入文件
                        f.write(imgData)
                        #图片写入完成关闭文件
                        f.close()
                        print("thread" + name + " write:" + pathfile)
                except:
                    print(str(name) + " thread write false:" + s)





