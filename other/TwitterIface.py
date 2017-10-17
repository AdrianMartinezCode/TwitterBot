import tweepy, twitter_db_connection

class TwitterIface:

	def __init__(self, consumer_key, consumer_secret, dbname):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.twitterdbcon = TwitterDbConnection(dbname)

	def authorize_twitter(self, access_key, access_secret):
		self.access_key = access_key
		self.access_secret = access_secret
		self.reload_auth()

	def reload_auth(self):
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_key, self.access_secret)
		self.api = tweepy.API(auth)

	def initdb(self, withtxt, file):
		self.twitterdbcon.initdb()
		if withtxt is True:
			self.twitterdbcon.insert_txt_file(file)


	def new_search(self):
		
