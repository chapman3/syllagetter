import re
import string
import collections

class textParser:
	def generate_dict(self, text):
		'''
		Usage: 
					Given a body of text (HTML or otherwise),
					returns an ordered dictionary of pairs in the format:
						{word:num_occurences,..}
		Args:
					text:	the body of text to be parsed
		Returns:	
					words:	ordered dictionary of word,occurence pairs
		'''
		#strip html tags
		no_html = re.sub('<.*?>', ' ', text)
		#strip punctuation
		no_punc = no_html
		no_punc = no_punc.replace("-", " ")
		for punc in string.punctuation:
			no_punc = no_punc.replace(punc, "")
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
	parser = textParser()
	text = "<p>These are words!</p><ul><li>And more words, and some symbols -> !@#$%^&*()</li></ul>"
	words = parser.generate_dict(text)
	for k, v in words.items():
		print k, v


if __name__ == "__main__":
	test()