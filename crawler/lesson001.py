import urllib
import urllib2

values = {}
values['username'] = "youxiafuture"
values['password'] = "youxia210046"

#字典的等价写法
#values = {"username":"","password":""}

data = urllib.urlencode(values)
url = "https://developer.android.com/index.html"

#url,data,timeout三个参数
#主要用于POST方法
#request = urllib2.Request(url,data)
#主要用于GET，拼接完成的url
request = urllib2.Request(url)
response = urllib2.urlopen(request)

print response.read()
