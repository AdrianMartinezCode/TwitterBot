# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

sys.path.append("/home/adrian/Dropbox/Bot_twitter/python/Oficial/twitterbot/twbot1/tweepybot")

import main_bot
from django.shortcuts import render
from django.http import HttpResponse
import tweepy


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def start(request):
	dt = main_bot.DaemonTwitter(1, "t")
	dt.init_api()
	#dt.add_related_words_from_web("http://rekink.com/terminology/glossary-of-kink-terminology-a-to-i/")
	dt.run()
	return HttpResponse("Started the service.")

# Create your views here.
