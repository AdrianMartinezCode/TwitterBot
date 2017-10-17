import re

def split_string(str):
	#return re.split("/([\w][\w']*\w)/g", str)
	return re.compile("([\w][\w]*'?\w?)").findall(str)
	#return re.split("/([a-zA-Z])\w+|([a-zA-Z])/g", str)

def ignore_special_chars(str):
	strfinal = ""
	first = True
	for w in re.compile("([\w-][\w]*'?\w?)").findall(str):
		if first:
			first = False
		else:
			strfinal += " "
		strfinal += w
	return strfinal


def list_string_lower(liststr):
	newlist = []
	for s in liststr:
		newlist.append(s.lower())
	return newlist

def set_hashtag(liststr):
	newlist = []
	for s in liststr:
		newlist.append('#' + s)
	return newlist

def build_tweet(liststr):
	tw = ""
	first = True
	for s in liststr:
		if first:
			first = False
		else:
			tw = tw + " "
		tw = tw + s
	return tw