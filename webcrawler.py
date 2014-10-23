#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import time
import datetime
from bs4 import BeautifulSoup

def crawl(stop, opt):
    url = 'http://www.dublinbus.ie/en/RTPI/Sources-of-Real-Time-Information/?searchtype=view&searchquery='
    # get time
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    # GET DATA SOURCE
    # Option 1: get data from Dublinbus website
    if opt == 1:
        header = {'User-Agent': 'Mozilla/5.0'} # Needed to prevent 403 error on Wikipedia
        req = urllib2.Request(url + str(stop),headers=header)
        response = urllib2.urlopen(req)
        # Let's make soup!!
        soup = BeautifulSoup(response)

    # Option2: get data from sample code
    elif opt == 2:
        sample_file = open('html_sample/262_21_48.html')
        sample = sample_file.read()
        # Let's make soup!!
        soup = BeautifulSoup(sample)
        # close sample_file
        sample_file.close()
    ## END - GET DATA SOURCE ##

    ## GET TABLES ##
    div = soup.find("div", {"id" : "stop-detail"})
    table = soup.find("table", { "id" : "rtpi-results" })

    f = open("temp"+str(stop)+".txt", "a")
    print "Name of the file: ", f.name

    ## OUTPUT TO SCREEN AND FILE
    print "\n================== Timestamp ==================\n"
    print st
    f.write("\nTimestamp: " + st)
    print "\n================== stop number and description ==================\n"
    f.write("\n==== stop number and description ====\n")
    for node in div.findAll('td'):
        print ''.join(node.findAll(text=True))
        f.write(''.join(node.findAll(text=True)))
    print "\n================== bus real time ==================\n"
    f.write("\n==== bus real time ====\n")
    for node in table.findAll('td'):
        print ''.join(node.findAll(text=True))
        f.write(''.join(node.findAll(text=True)))
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
    
    # Get bus stop no.
    bus = raw_input('''What bus stop no. you're looking for: ''')
    # Try to convert it to a float
    try:
        bus = float(bus)
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
        crawl(int(bus), 1)
        time.sleep(num)
        print('After: %s\n' % time.ctime())
        print('END REPEATING No. ' + str(i) + '\n')

# TO DO:
# add wait method (wait for 60 seconds) √
# while loop √
# regex to extract and format info
# data structure
# a better interface √
# more parameters to method √



