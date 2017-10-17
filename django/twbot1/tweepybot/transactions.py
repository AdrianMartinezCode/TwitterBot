
import sys

#sys.path.append("/home/adrian/Dropbox/Bot_twitter/python/Oficial/twitterbot/twbot1")

from twbot1.models import *
from django.core.exceptions import ObjectDoesNotExist
import wordparser
import tweepy
import imageseeker


class TxSearch():

	def __init__(self, api):
		self.api = api

	def execute(self):
		#search the 1th word in bd by number of seeked (the '-' indicates descending order, ascending is implied)
		word = RelatedWord.objects.order_by('seeked')[0]

		print(word.word)
		#get the first tweet by id in decreased order
		try:
			lasttweet = word.tweets.order_by('-id')[0]
			thattweets = self.api.search(q = word.word, since_id = lasttweet.id)
		except:
			print word.word
			thattweets = self.api.search(q = word.word)
			#self.api.search(q = word.word, since_id = 909775453593980929)
		#retrieve from the API twitter the tweet related with word (extracting the first tweet from the list of tweets)
		
		if len(thattweets) == 0:
			return
		thattweet = thattweets[0]

		print(thattweet.text)

		#extract the words from the text of tweet
		liststring = wordparser.split_string(str = thattweet.text)

		#to lower case every word
		listwordplain = wordparser.list_string_lower(liststr = liststring)


		usrid = thattweet.author.id
		try:
			usr = User.objects.get(pk = usrid)
		except ObjectDoesNotExist:
			usr = User.objects.create(id = usrid)
		usr.save()


		try:
			twt = Tweet.objects.get(pk = thattweet.id)
		except ObjectDoesNotExist:
			twt = Tweet.objects.create(id = thattweet.id)
		twt.userr = usr
		twt.save()

		for s in listwordplain:
			try:
				wd = Word.objects.get(pk = s)
				wd.finded = wd.finded + 1
			except ObjectDoesNotExist:
				wd = Word.objects.create(word = s)
			wd.tweets.add(twt)
			wd.save()

		word.seeked = word.seeked + 1
		word.save()


class TxPost():
	def __init__(self, api, maxchars, path):
		self.api = api
		self.maxchars = maxchars
		self.path = path

	def exists_link(self, link):
		try:
			Image.objects.get(pk = link)
			return False
		except ObjectDoesNotExist:
			return True

	def execute(self):
		#retrieve the word to seek the image, the less seeked
		rel_word = RelatedWord.objects.order_by('seeked')[0]

		#last tweet seeked
		lasttweet = Word.objects.order_by('-finded')[0].tweets.order_by('-id')[0]

		text = ""
		used_words = []
		used_words_real = []
		#all the words related ordered by the published times
		all_words = RelatedWord.objects.order_by('published')

		#calculate the length of tweet and include the words
		"""it = iterator(all_words)
		count = 0
		w = it.next()
		while(count + len(w.word) + 2 < self.maxchars):
			used_words.append(w.word)
			used_word_real.append(w)
			count = count + len(w.word) + 2
			w = it.next()"""

		usr_tw = self.api.get_user(lasttweet.userr.id)

		count = len(usr_tw.screen_name) + 1
		for w in all_words:
			if count + len(w.word) + 2 >= self.maxchars:
				break
			used_words.append(w.word)
			used_words_real.append(w)
			count = count + len(w.word) + 2


		print(used_words)
		#set the tweet	
		hash_words = wordparser.set_hashtag(used_words)
		tw = wordparser.build_tweet(hash_words)
		#tw += " @" + usr_tw.screen_name

		try:
			link_image = imageseeker.get_image(rel_word.word, self.path, self.exists_link)
		except:
			return
		print(link_image)
		try:
			img = Image.objects.create(url = link_image)
		except:
			img = Image.objects.get(pk = link_image)


		#tpri = TPRI.objects.create(tweets = lasttweet, relatedWords = rel_word, images = img)
		
		"""img.tpri.add(tpri)
		lasttweet.tpri.add(tpri)
		rel_word.tpri.add(tpri)"""

		for us in used_words_real:
			us.published += 1
			us.save()

		img.save()
		lasttweet.save()
		rel_word.seeked += 1
		rel_word.save()

		print(tw)
		print(lasttweet.id)


		self.api.update_with_media(self.path, status = tw, in_reply_to_status_id = lasttweet.id)
		
		#self.api.update_with_media(path = self.path, status = tw, in_reply_to_status_id = lasttweet.id)
		

class TxAddRelatedWords():
	def __init__(self, path):
		self.path = path

	def execute(self):
		inputf = open(self.path)
		for w in inputf:
			RelatedWord.objects.create(word = w)
		inputf.close()

	def execute_fromlist(self, listw):
		for w in listw:
			try:
				RelatedWord.objects.create(word = w)
			except:
				pass