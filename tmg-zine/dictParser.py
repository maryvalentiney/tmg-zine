import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import ssl
import sys
import getopt
import itertools
import re


stop_words = set(stopwords.words('english'))


def removeDups(myList):
	newList = []
	for i in myList:
		if i not in newList:
			newList.append(i)
	return newList

def returnWords(line):
	new_words = []
	words = nltk.word_tokenize(line)
	for wrd in [word.lower() for word in words]:
		if not wrd in stop_words:
			new_words.append(wrd)

	return new_words

inFile = open(sys.argv[1], "r")
lines = inFile.read()
inFile.close()
wordList = []

# for line in lines:
wordList = returnWords(lines)
wordList = removeDups(wordList)
for words in wordList:
    if words.isalpha():
        print(words)
