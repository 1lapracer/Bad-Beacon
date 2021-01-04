#!/usr/bin/env python3

import requests as req
import time
import random

################################################################################
#config values                                                                 #
################################################################################

#set jitter yes (1) or no (0)
jitter = 1
#randomness of jitter in seconds
jittertime = 5
#website to call
sitename = "http://www.webcode.me"
#port to make call on
siteport = "80"
#connection timeout value
timeoutx = 1


# Get user input
num = input('How long to wait: ')

try:
    num = float(num)
except ValueError:
    print('Please enter in a number.\n')

#Set site to call
sitename = sitename +":" + siteport
print(sitename)




def sleeper():

    while True:
        import requests as req

        print('Before: %s' % time.ctime())

        if jitter == 1:
            print("hit jitter")
            jitterset = float(random.randint(0,jittertime))
            time.sleep(jitterset)

        time.sleep(num)

        try:
            resp = req.get(sitename, timeout=timeoutx)
            #print(resp.text)
        except:
             print ("http error")

        print('After: %s' % time.ctime())



try:

    sleeper()

except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()