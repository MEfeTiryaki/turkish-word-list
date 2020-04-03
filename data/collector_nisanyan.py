#!/usr/bin/python
# -*- coding: utf8 -*-

import urllib2
import re

alphabet = u"ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"

def readPage(word):
	# https://www.nisanyansozluk.com/?k=baba&view=annotated
	url = u"https://www.nisanyansozluk.com/?k="+word.decode('utf-8')+"&view=annotated"
	header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-9,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

	req = urllib2.Request(url.encode('utf-8'), headers = header)
	try:
	    page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.fp.read()
	content = page.read()
	try:
		words  = content.split("hghlght\">")[1].split("</tr>")[0]
	except:
		print(word+" does't exist!")
		return None
	_word = words.split("td title=\"")[1].split("\"")[0]
	print(_word)
	history = words.split("<div class=\"eskoken\"><div class=\"blmbasi\">Tarihçe <span style=\"font-weight:normal\">(tespit edilen en eski Türkçe kaynak ve diğer örnekler)</span></div>")[1].\
					split("</div><div class=\"eskoken\">")[0]
	root = re.findall('<div class=\"eskoken\"><div class=\"blmbasi\">Köken</div>(.*?)</div><div class=\"eskoken\">', words)[0]

	print("History : " + history)
	# print("Origin : ")
	# print(root)

	originLang =  re.findall('<b>(.*?)</b>', root)
	originWord =  re.findall('<i>(.*?)</i>', root)
	historicalRecords = [x.split(",") for x in re.findall('\[(.*?)\]', history)]
	historicalExamples = [x.split(",") for x in re.findall('<u>(.*?)</u>', history)]

	print(originLang[0])
	print(originWord[0])
	print(originLang)
	print(historicalRecords)
	print(historicalExamples)
	return words

def getWordList():
	words = []
	for letter in alphabet:
		words += readPage(letter)
	return words

def writeToFile(filename):
	f = open(filename, 'w')
	f.write("\n".join(getWordList()))
	f.close()

# writeToFile("words.txt")
def main():
	readPage("ayak")

if __name__ == '__main__':
	main()
