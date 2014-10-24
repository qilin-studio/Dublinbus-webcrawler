#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webcrawler
import time

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
        webcrawler.crawl(int(bus), 1)
        time.sleep(num)
        print('After: %s\n' % time.ctime())
        print('END REPEATING No. ' + str(i) + '\n')

# TO DO:
# add wait method (wait for 60 seconds) √
# while loop √
# regex to extract and format info √
# a better interface √
# more parameters to method √