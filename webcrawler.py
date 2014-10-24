#!/usr/bin/env python

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