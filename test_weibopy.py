import logging

from weiboLogin import weiboLogin, postData, getData
from weibo import APIClient

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d]\n\t%(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='example.log'
)

APP_KEY = "3226611318"
APP_SECRET = "4f94b19d1d30c6bce2505e69d22cd62e"
CALLBACK_URL = "https://api.weibo.com/oauth2/default.html"

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

# https://api.weibo.com/oauth2/authorize?response_type=code&redirect_uri=https%3A//api.weibo.com/oauth2/default.html&client_id=3226611318
url = client.get_authorize_url()

logging.info("Auth url: %s" % url)
#
# weiboLogin("ichen0201@sina.com", "s2013h1cfr")
#
# client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
#
# r = client.request_access_token("8ed89095d5fc6fd697f137bc0dbb93cf")
#
# access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
# expires_in = r.expires_in  # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
#
# # TODO: 在此可保存access token
# client.set_access_token(access_token, expires_in)
#
# print(client.statuses.user_timeline.get())
# print(client.statuses.update.post(status=u'测试OAuth 2.0发微博'))
# print(client.statuses.upload.post(status=u'测试OAuth 2.0带图片发微博', pic=open('/Users/michael/test.png')))
