__author__ = 'Fly'
# -*- coding: utf-8 -*-
from weibo import APIClient
# import urllib2
import urllib

#APP_KEY和APP_SECRET，需要新建一个微博应用才能得到
APP_KEY = '3226611318'
APP_SECRET = '4f94b19d1d30c6bce2505e69d22cd62e'
#管理中心---应用信息---高级信息，将"授权回调页"的值改成https://api.weibo.com/oauth2/default.html
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
AUTH_URL = 'https://api.weibo.com/oauth2/authorize'


def getData(url) :
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    text = response.read().decode('utf-8')
    return text

def postData(url , data) :
    headers = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'}
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url , data , headers)
    response = urllib.request.urlopen(request)
    text = response.read().decode('utf-8')
    return text


def GetCode(userid,passwd):
    client = APIClient(app_key = APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    referer_url = client.get_authorize_url()
    postdata = {
        "action": "login",
        "client_id": APP_KEY,
        "redirect_uri":CALLBACK_URL,
        "userId": userid,
        "passwd": passwd,
        }

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Referer":referer_url,
        "Connection":"keep-alive"
    }
    req  = urllib.request.Request(
        url = AUTH_URL,
        data = urllib.parse.urlencode(postdata).encode('utf-8'),
        headers = headers
    )
    resp = urllib.request.urlopen(req).read()
    return resp.decode('utf-8')
    #return resp.geturl()[-32:]
    
if __name__ == "__main__":
    #print(GetCode("ichen0201@sina.com","s2013h1cfr"))
    print(getData("https://api.weibo.com/oauth2/authorize?client_id=3226611318&redirect_uri=https%3A//api.weibo.com/oauth2/default.html&response_type=code"))