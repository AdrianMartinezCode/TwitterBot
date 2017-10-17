# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models


class User(models.Model):
	id = models.IntegerField(primary_key = True)


class Tweet(models.Model):
	id = models.IntegerField(primary_key = True)
	userr = models.ForeignKey(User, null = True)
	#tpri = models.ForeignKey(TPRI, null = True)

class Word(models.Model):
	word = models.TextField(primary_key = True)
	tweets = models.ManyToManyField(Tweet, null = True)
	finded = models.IntegerField(default = 1)

	#used = models.IntegerField(default = 0)

	#def search(self, api):
		

class RelatedWord(Word):
	seeked = models.IntegerField(default = 0)
	published = models.IntegerField(default = 0)
	#tpri = models.ForeignKey(TPRI, null = True)

class Image(models.Model):
	url = models.URLField(primary_key = True)
	#tpri = models.ForeignKey(TPRI, null = True)


class TPRI(models.Model):
	tweets = models.ForeignKey(Tweet, null = False, primary_key = True)
	relatedWords = models.ForeignKey(RelatedWord, null = False)
	images = models.ForeignKey(Image, null = False)
	#complementariesWords = models.ManyToManyField(RelatedWord)

	#tweett = models.IntegerField(primary_key = True, null = False)
	#relatedWordd = models.TextField(null = False)
	#imagee = models.URLField(null = False)

	class Meta:
		unique_together = ('tweets', 'relatedWords', 'images')
