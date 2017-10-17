from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json
from custom_exceptions import ExceptionErrorOnLoadingImg


def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def get_soup_props(prop):
	return json.loads(prop.text)["ou"], json.loads(prop.text)["ity"]

def get_image(word, directory, consultant):
	query = word#raw_input("porn")# you can change the query for the image  here
	image_type="ActiOn"
	query= query.split()
	query='+'.join(query)
	url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

	#add the directory for your image here
	DIR = directory#DIR="Pictures"
	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
	soup = get_soup(url,header)

	file_h = open(os.path.join(".", "pagina.html"), 'wb')
	file_h.write(urllib2.urlopen(urllib2.Request(url,headers=header)).read())
	file_h.close()

	#ActualImages=[]# contains the link for Large original images, type of  image

	info = soup.find_all("div", {"class" : "rg_meta"});

	"""
	it = iterator(info)

	link, Type = get_soup_props(it.next())
	while(consultant(link)):
		link, Type = get_soup_props(it.next())"""

	for it in info:
		link, Type = get_soup_props(it)
		#print link
		if (not consultant(link)):
			break

	try:
		req = urllib2.Request(link, headers={'User-Agent' : header})
		raw_img = urllib2.urlopen(req).read()
		f = open(DIR, "wb")
		f.write(raw_img)
		f.close()
	except Exception as e:
		raise ExceptionErrorOnLoadingImg("Error on downloading the image", 1)

	return link