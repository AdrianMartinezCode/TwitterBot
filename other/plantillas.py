from django.db import models

class User(models.Model):
	id = models.IntegerField(primary_key = True)

class Tweet(models.Model):
	id = models.IntegerField(primary_key = True)
	users = models.ForeignKey(User)

class Word(models.Model):
	word = models.TextField(primary_key = True)
	tweets = models.ManyToManyField(Tweet)
	users = models.ManyToManyField(User)

class RelatedWord(Palabras):
	seeked = models.IntegerField()
	#published = models.IntegerField()

class Image(models.Model):
	url = URLField(primary_key = True)

class TPRI(models.Model):
	tweets = models.ForeignKey(Tweet, null = False)
	relatedWords = models.ForeignKey(RelatedWord, null = False)
	images = models.ForeignKey(Image, null = False)
	complementariesWords = models.ManyToManyField(RelatedWord) 
