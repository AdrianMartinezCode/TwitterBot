import requests
from bs4 import BeautifulSoup

def get_related_words(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")

	list_word = []
	for td in soup.findAll("strong"):
		list_word.append(td.text)

	return list_word