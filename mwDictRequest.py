import requests

class mwDictRequest:
	def __init__(self):
		self.endpoint, self.key = self.load_settings()

	def load_settings(self):
		keyfile = open("key.txt","r")
		endpoint = keyfile.readline().strip()
		key = keyfile.readline().strip()
		return endpoint, key

	def make_request(self,word):
		#make request using endpoint and key, return pronunciation tag
		#TO-DO: handle for "suggestions" when word not found
		url = self.endpoint + word + "?key=" + self.key
		r = requests.get(url)
		xml = r.text
		syl_count = self.request_helper(xml)
		return syl_count

	def request_helper(self, xml):
		#used to parse response object
		pr_start = xml.find("<pr>")
		if pr_start > 0:
			pr_end = xml.find("</pr>")
			comma_check = pr_start + xml[pr_start:].find(",")
			if comma_check < pr_start:
				comma_check = pr_end
			return xml[pr_start:min(comma_check,pr_end)].count("-") + 1
		else:
			return None

def test():
	req_obj = mwDictRequest()
	tests = {"tester": 2, "appreciate":4, "journal":2, "planetarium":5, "handle":2}
	for test in tests:
		assert int(tests[test]) == int(req_obj.make_request(test))

if __name__ == "__main__":
	test()