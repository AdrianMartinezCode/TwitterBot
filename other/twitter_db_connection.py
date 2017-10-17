import sqlite3

class TwitterDbConnection:

	TABLENAME_WORDS = "WORDS"
	QUERY_DELETE_TABLE_WORDS = "DROP TABLE IF EXISTS " + TABLENAME_WORDS
	QUERY_CREATE_TABLE_WORDS = "CREATE TABLE IF NOT EXISTS " + TABLENAME_WORDS + " (word TEXT PRIMARY KEY, count INTEGER)"
	QUERY_EXISTS_WORD = "SELECT * FROM " + TABLENAME_WORDS + " WHERE word = ?"
	QUERY_INSERT_NEW_WORD = "INSERT INTO " + TABLENAME_WORDS + " VALUES(?, 1)"
	QUERY_UPDATE_WORD = "UPDATE FROM " + TABLENAME_WORDS + " SET count = count + 1 WHERE word = ?"

	TABLENAME_ANALISED_TWEET = "ANALISEDTWEET"
	QUERY_CREATE_TABLE_ANALISED_TWEET = "CREATE TABLE IF NOT EXISTS " + TABLENAME_ANALISED_TWEET + " (id INTEGER PRIMARY KEY, date DATETIME DEFAULT CURRENT_TIMESTAMP)"
	QUERY_DELETE_TABLE_ANALISED_TWEET = "DROP TABLE IF EXISTS " + TABLENAME_ANALISED_TWEET
	QUERY_INSERT_NEW_TWEET = "INSERT INTO " + TABLENAME_ANALISED_TWEET + " (id) VALUES(?)"

	TABLENAME_ANALISED_USER = "ANALISEDUSER"
	QUERY_CREATE_TABLE_ANALISED_USER = "CREATE TABLE IF NOT EXISTS " + TABLENAME_ANALISED_USER + " (id INTEGER PRIMARY KEY)"
	QUERY_DELETE_TABLE_ANALISED_USER = "DROP TABLE IF EXISTS " + TABLENAME_ANALISED_USER
	QUERY_INSERT_NEW_USER = "INSERT INTO " + 

	def __init__(self, dbname):
		self.dbname = dbname

	def resetdb(self):
		curs.execute(QUERY_DELETE_TABLE)
		conn.commit()
		self.initdb()

	def initdb(self):
		self.conn = sqlite3.connect(self.dbname)
		curs = self.conn.cursor()
		curs.execute(QUERY_CREATE_TABLE)
		conn.commit()

	def insert_txt_file(self, file):
		with open(file, "r") as ins:
			curs = self.conn.cursor()
			for word in ins:
				self.__set_word(word, curs)
			conn.commit()

	def __set_word(self, word, cursor):
		cursor.execute(QUERY_EXISTS_WORD, word)
		if cursor.fetchone() is None:
			cursor.execute(QUERY_INSERT_NEW_WORD, word)
		else:
			cursor.execute(QUERY_UPDATE_WORD, word)




