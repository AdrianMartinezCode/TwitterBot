#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'hHUWlXFqXBqOzSsbADwFDiIMh'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'pNNKNhgK1hyRzmqDFXI8meq7f67kPUSmKl3QEbcAXNXyk09PT2'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '887284662-B8ot2sArpEWBwCKXTsLdLfUU8IHiwHYA6XNsIktJ'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'USsAu9YQHlOESP6PcqDRCmjoQVkqMPfj2ZChLTfR20Vh7'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    #time.sleep(1)#Tweet every 15 minutes