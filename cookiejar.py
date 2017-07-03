import urllib2
import cookielib
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar("locale=zh-CN; _fofapro_ars_session=330sddsd1471d2e6643")
#cookie = "locale=zh-CN; _fofapro_ars_session=330b83bee72e84fbf2eeb1471d2e6643"
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('https://fofa.so/result?q=%22Powered+by+vancheer%22&qbase64=IlBvd2VyZWQgYnkgdmFuY2hlZXIi&page=4')
print response.read()
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value