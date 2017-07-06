# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import requests

#自动处理cookie
requests.Session()
#允许重定向
r = requests.get('http://github.com', allow_redirects=False)

#控制代理，headers
proxy = {"https": "https://127.0.0.1:8080"}
r = requests.get(url, headers = headers, proxies = proxy)

#禁用ssl warning
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

