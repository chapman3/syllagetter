import re
import string
import sys
import collections

def generateDict(text):
	'''
	Given a body of text (HTML or otherwise), returns an ordered dictionary of pairs in the format [word:num_occurences]
	'''
	#strip html tags
	no_html = re.sub('<.*?>', ' ', text)
	#strip punctuation
	no_punc = no_html
	no_punc = no_punc.replace("-"," ")
	for p in string.punctuation:
		no_punc = no_punc.replace(p,"")
	#split text into words
	word_array = no_punc.lower().split()
	#create dict
	words = collections.OrderedDict()
	for word in word_array:
		if word in words.keys():
			words[word] += 1
		else:
			words[word] = 1
	return words

def test():
	text = "<p>These are words!</p><ul><li>These-These These are list items.</li><li>And then, is this, another.. list item??</li></ul>And more words, and some symbols -> !@#$%^&*()"
	words = generateDict(text)
	for k,v in words.items():
		print k,v

if __name__ == "__main__":
	test()