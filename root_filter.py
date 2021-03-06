#!/usr/bin/python
# -*- coding: utf8 -*-


import re
import time

alphabet = u"ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"



def readFile (filename):
	f = open(filename, 'r')
	list_ = []
	for line in f:
		list_.append(line[:-1])
	return list_

def printWords(words):
	k = 0
	while k< 20:
		print(words[k]+str(len(words[k].split(" "))) )

		k+=1

def oneWordOnly(W):
	R =[]
	for w in W:
		if len(w.split(" ")) < 2:
			R.append(w)
	return R

def fiterTuremis(W,S):
	R = W
	temp =[]
	
	for w in W:
		for s in S:
			if w[-len(s):]==s:
				if len(w)-len(s)>=2:		
					with open("compound_words/"+s+".txt", "a") as myfile:
	   					myfile.write(w+"\n")
					temp.append(w)
	for t in temp:
		R.remove(t)			
	return R

def writeFile(filename,W):
	f = open(filename, 'w')
	f.write("\n".join(W))
	f.close()

def appendFile(filename,W):
	for w in W:	
		with open(filename, "a") as f:
	   		f.write(w+"\n")

def deleteTuremis(S):
    for s in S:
    	with open("compound_words/"+s+".txt", "w"):
        	pass

def createEylemler():
	mek_ = readFile('compound_words/mek.txt')
	mak_ = readFile('compound_words/mak.txt')
	verbs  = []
	
	for v in mek_:
		verbs.append(v[:-3])
	for v in mak_:
		verbs.append(v[:-3])
	
	writeFile("verbs.txt",verbs)
	

words = []
subfices = []
roots = []

start = time.time()
words = readFile('data/words.txt')
subfices = readFile('data/subfices.txt') 
deleteTuremis(subfices)

# Filter out
one_words = oneWordOnly(words)
roots = fiterTuremis(one_words,subfices)

# Write in file
writeFile('roots.txt',roots)

# Create verbs 
createEylemler()

end = time.time()

print(end - start)









