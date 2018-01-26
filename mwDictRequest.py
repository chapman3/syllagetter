class mwDictRequest:
	def __init__(self):
		self.endpoint, self.key = self.load_settings()

	def load_settings():
		keyfile = open("key.txt",r)
		endpoint = keyfile.readline()
		key = keyfile.readline()
		return endpoint, key

	def make_request(word):
		#make request using endpoint and key, return pronunciation tag
		return

	def request_helper():
		#used to parse response object
		return

def test():
	req_obj = mwDictRequest()
	print req_obj.make_request("tester")

if __name__ == "__main__":
	test()