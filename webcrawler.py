#!/usr/bin/env python

import urllib2
import time
import datetime
from bs4 import BeautifulSoup

def crawl(url, opt):
    # get time
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    # GET DATA SOURCE
    # Option 1: get data from Dublinbus website
    if opt == 1:
        header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
        req = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(req)
        # Let's make soup!!
        soup = BeautifulSoup(response)

    # Option2: get data from sample code
    elif opt == 2:
        sample_file = open('sample/262_21_48.html')
        sample = sample_file.read()
        # Let's make soup!!
        soup = BeautifulSoup(sample)
        # close sample_file
        sample_file.close()
    ## END - GET DATA SOURCE ##

    ## GET RAW TABLES ##
    div = soup.find("div", {"id" : "stop-detail"})
    table = soup.find("table", { "id" : "rtpi-results" })
    print "================== What's the time now? =================="
    print st
    print "================== [raw] stop number and description =================="
    print div
    print "================== [raw] bus real time =================="
    print table
    print "================== end of table =================="
    print st
    ## END - GET RAW TABLES ##

    ## OUTPUT SOURCE CODE ##
    # output source code to a temp file
    file = open("temp.txt", "a")
    print "Name of the file: ", file.name
    
    file.write("\n\n>>>>>>>>>>>>>Timestamp: " + st + " <<<<<<<<<<<<<<<<<\n")
    file.write("\n================== [raw] stop number and description ==================\n")
    for line in div.prettify("latin-1"):      
        file.write(line)
    file.write("\n================== [raw] bus real time ==================\n")
    for line in table.prettify("latin-1"):      
        file.write(line)
    file.write("\n================== end of table ==================\n")
    file.write("\n>>>>>>>>>>>>>Timestamp: " + st + " <<<<<<<<<<<<<<<<<\n")
    
    file.close()
    ## END - OUTPUT SOURCE CODE ##


## Let's make our webcrawler busy ##
while True:
    # Get time between request
    num = raw_input('How long to wait: ')
    # Easy way to stop this process
    if num in ('quit','q','Quit','Q'):
        print('QUIT')
        exit()
    # Try to convert it to a float
    try:
        num = float(num)
    except ValueError:
        print('Please enter in a number.\n')
        continue
    
    # Get times to repeat request 
    count = raw_input('How many time to repeat: ')
    # Try to convert it to a float
    try:
        count = float(count)
    except ValueError:
        print('Please enter in a number.\n')
        continue
    count = int(count)
    for i in range(0, count):      
        # Run our time.sleep() command,
        # and show the before and after time
        print('REPEATING No. ' + str(count))
        print('Before: %s' % time.ctime())
        crawl('http://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=262', 2)
        time.sleep(num)
        print('After: %s\n' % time.ctime())
        print('END REPEATING No. ' + str(count))



# TO DO:
# add wait method (wait for 60 seconds) √
# while loop √
# regex




