
def generateDict(text):
	'''
	Given a body of text (HTML or otherwise), returns an ordered dictionary of pairs in the format [word:num_occurences]
	'''
	#strip html tags
	#strip punctuation
	#split text into words
	#create dict
	words = Collections.OrderedDict()
	return words

def test():
	text = ""
	words = generateDict(text)
	for k,v in words.items():
		print k,v

if __name__ == "__main__":
	test()