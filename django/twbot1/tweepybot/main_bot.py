import transactions
import my_parser
import wordparser
import threading
import os
import signal
import tweepy
import traceback
import sys

class DaemonTwitter:
	def __init__(self, dId, name):
		self.dId = dId
		self.name = name
		self.flag = 0 #if flag = 1, the daemon must stop
		self.init_api()

	def init_api(self):
		CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
		CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
		ACCESS_KEY = ''#keep the quotes, replace this with your access token
		ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		self.api = tweepy.API(auth)

	def add_related_words(self, path):
		tx = transactions.TxAddRelatedWords(path = path)
		tx.execute()

	def add_related_words_from_web(self, url):
		words = my_parser.get_related_words(url)
		newlist = []
		for w in words:
			newlist.append(wordparser.ignore_special_chars(w))
		tx = transactions.TxAddRelatedWords(path = url)
		tx.execute_fromlist(newlist)

	def stop_thread(self):
		self.flag = 1

	def run(self):
		#count_tw = 0
		
		pid = os.fork()
		if pid > 0:
			return

		while self.flag == 0:
			txSearch = transactions.TxSearch(api = self.api)
			txSearch.execute()
			print("He buscado")

			#that_path = os.path.join(os.getcwd(), "imagetemp.jpg")
			that_path = os.path.join("imagetemp.jpg")
			txPost = transactions.TxPost(api = self.api, maxchars = 140, path = that_path)
			txPost.execute()
			#os.remove(that_path)
			print("He posteado")
				
		


