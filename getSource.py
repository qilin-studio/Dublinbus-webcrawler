#!/usr/bin/env python

import urllib2

url = 'http://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=262' # write URL here
      
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read() 
print the_page

file = open("output.txt", "w")
print "Name of the file: ", file.name

for line in the_page:
    file.write(line)

file.close()