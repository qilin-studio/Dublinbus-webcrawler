#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

## get source code from a specific website ##
url = 'http://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=262' # write URL here

# DATA SOURCE
# Option 1: get data from Dublinbus website
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(url,headers=header)
response = urllib2.urlopen(req)

# Option2: get data from sample code
sample_file = open('sample/262_21_48.html')
sample = sample_file.read()
sample_file.close()


# Let's make soup!!
# change parameter "response" to "sample" if the Dublin bus table is empty
soup = BeautifulSoup(sample)

## end - get source code ##

## grab raw tables ##

div = soup.find("div", {"id" : "stop-detail"})
table = soup.find("table", { "id" : "rtpi-results" })

print "================== [raw] stop number and description =================="
print div
print "================== [raw] bus real time =================="
print table
print "================== end of table =================="


# output source code to a temp file
file = open("temp.txt", "w")
print "Name of the file: ", file.name

for line in soup.prettify("latin-1"):
    file.write(line)

file.close()
# end - output temp file

