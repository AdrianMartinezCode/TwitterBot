#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys

usr_id = "Piltraa1"
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


tl = api.friends_ids(usr_id)

for fr in tl:
	print(fr)
	api.destroy_friendship(fr)
