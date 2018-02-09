import dbOperations
import mwDictRequest
import textParser

class syllagetter:
	def __init__(self, log):
		'''
		syllagetter object constructor
		takes a log file as an argument to record results
		'''
		self.req_obj = mwDictRequest.mwDictRequest()
		self.connection = dbOperations.connect()
		self.text_parser = textParser.textParser()
		self.log = log
	
	def get_syl_count(self, text):
		'''
		Usage: 
					uses textParser mwDictRequest and dbOperations to 
					calculate total syllable count of a body of text.
		Args:
					text:	text to get syllable count from
		Returns:	
					syl_count:	syllable count result from text block. 
								log file will record results as well.
		'''
		self.log.write("====  NEW ENTRY  ====\n")
		self.log.write("Full Text | " + text + "\n")
		words = self.text_parser.generate_dict(text)
		syl_count = 0
		for word, occur in words.items():
			db_check = dbOperations.get_syl(self.connection, word)
			if db_check == None:
				mw_check = self.req_obj.make_request(word)
				if mw_check == None:
					self.log.write("Word not found | " + str(word) + " | occurences: " + str(occur) + "\n")
				else:
					dbOperations.add(self.connection, word, mw_check, self.log)
					syl_count += mw_check * occur
			else:
				syl_count += db_check * occur
		self.log.write("Syllable Count | " + str(syl_count) + "\n")
		return syl_count

def test():
	log = open("log-syllagetter-test.txt", "w")
	lines = open("testWords.txt", "r")
	syllagetter_obj = syllagetter(log)
	try:
		for line in lines:
			print syllagetter_obj.get_syl_count(line)
	except Exception as e:
		print "Exception encountered, see logfile"
		log.write("Exception: " + str(e))

if __name__ == "__main__":
	test()