# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import requests
import json

# http://lbsyun.baidu.com/index.php?title=webapi/high-acc-ip

ip_addr = raw_input('Your ip:')
url = 'http://api.map.baidu.com/highacciploc/v1?qcip=%s&qterm=pc&ak=omhNrOPQOYt5iVzNSlZ8MuE6tQC7KxL2&coord=bd09ll&extensions=3' % (ip_addr)
r = requests.get(url)
content = json.loads(r.content)
print content['content']
print content['content']['formatted_address']