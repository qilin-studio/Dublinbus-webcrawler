import urllib, time, datetime


ttdurl = "/cgi-bin/rtpi/timetableinformation?"
host = "www.dublinked.ie"
header = "http://[username]:[password]@"
ttdquery = urllib.urlencode({'type': 'day', 'stopid': '262', 'operator': 'bac', 'format': 'xml'})

rturl = "/cgi-bin/rtpi/realtimebusinformation?"
host = "www.dublinked.ie"
header = "http://[username]:[password]@"
rtquery = urllib.urlencode({'stopid': '184', 'routeid': '4', 'operator': 'bac', 'format': 'xml'})

request = header + host + rturl + rtquery

ts1 = time.time()
st1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')

f = urllib.urlopen(request)
g = str(f.read())

ts2 = time.time()
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')

print g

print st1
print st2