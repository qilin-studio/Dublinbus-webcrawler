#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        header = {'User-Agent': 'Mozilla/5.0'} # Needed to prevent 403 error on Wikipedia
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

    ## GET TABLES ##
    div = soup.find("div", {"id" : "stop-detail"})
    table = soup.find("table", { "id" : "rtpi-results" })

    file = open("temp262.txt", "a")
    print "Name of the file: ", file.name

    ## OUTPUT TO SCREEN
    print "\n================== Timestamp ==================\n"
    print st
    file.write("\nTimestamp: " + st)
    print "\n================== stop number and description ==================\n"
    file.write("\n==== stop number and description ====\n")
    for node in div.findAll('td'):
        print ''.join(node.findAll(text=True))
        file.write(''.join(node.findAll(text=True)))
    print "\n================== bus real time ==================\n"
    file.write("\n==== bus real time ====\n")
    for node in table.findAll('td'):
        print ''.join(node.findAll(text=True))
        file.write(''.join(node.findAll(text=True)))
    ## END - OUTPUT 

## Let's make our webcrawler busy ##
while True:
    # Get time between request
    num = raw_input('How long to wait or quit: ')
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
    for i in range(1, count+1):      
        # Run our time.sleep() command,
        # and show the before and after time
        print('\nREPEATING No. ' + str(i))
        print('Before: %s' % time.ctime())
        crawl('http://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery=262', 1)
        time.sleep(num)
        print('After: %s\n' % time.ctime())
        print('END REPEATING No. ' + str(i) + '\n')

# TO DO:
# add wait method (wait for 60 seconds) √
# while loop √
# regex to extract and format info
# data structure
# a better interface



