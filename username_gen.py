#python

import datetime


now = datetime.datetime.now()

for i in range(0,365*3):
    date = now + datetime.timedelta(days=-i)
    str = date.strftime("%y%m%d")
    print str + '01'
    print str + '02'
    print str + '03'
