import urllib2

url = raw_input("Please Input URL:")
cookie = raw_input("Please Input cookie")
request = urllib2.Request('https://fofa.so/result?q=%22Powered+by+vancheer%22&qbase64=IlBvd2VyZWQgYnkgdmFuY2hlZXIi&page=4')
request.add_header('Cookie', 'locale=zh-CN; _fofapro_ars_session=330b83bee72e84fbf2eeb1471d2e6643')
response = urllib2.urlopen(request)

print response.read()