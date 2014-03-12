import urllib3
from lxml import etree

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.whitehouse.gov/schedule/president/feed')
if r.status == 200:
    print r.data
