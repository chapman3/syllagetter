import sqlite3

def init():
	'''
	Usage: 
			creates the wordbank.db database
	Args:
			none
	Returns:	
			1 if created
			0 if already existed
	'''
	try:
		print("Initialising Database")
		connection = connect()
		print("Creating Inventory Table")
		sql_command = """CREATE TABLE wordbank (word VARCHAR(30) PRIMARY KEY, syl_count INTEGER);"""
		cursor = connection.cursor()
		print("Executing")
		cursor.execute(sql_command)
		connection.commit()
		print("Completed")
		cursor.close()
		connection.close()
		print("Connections Closed")
		return 1
	except:
		print("Database Already Initialized")
		return 0

def get_syl(connection, word):
	'''
	Usage:
				searches database for a word, returns syllable count if found
	Args:
				connection:	sqlite3 wordbank.db connection
				sku:		word to be searched
	Returns:
				syllable count if word found
				None if word not found
	'''
	cursor = connection.cursor()
	retVal = cursor.execute("SELECT syl_count FROM wordbank WHERE word =?", (word,)).fetchone()
	cursor.close()
	if retVal == None:
		return None
	else: 
		return retVal[0]

def add(connection, word, syl_count, log):
	'''
	Usage: 
			adds word, syl_count pairs to database
	Args:		
			connection:	sqlite3 wordbank.db connection
			word:		word to be added
			syl_count:	syl_count to be associated to word
			log:		logfile to record any errors
	Returns:
			none, updates database with new words
	'''
	cursor = connection.cursor()
	sql_command = "INSERT INTO wordbank (word, syl_count) VALUES (?, ?);"
	try:
		cursor.execute(sql_command, (word, syl_count))
		connection.commit()
	except Exception as e:
		print("Could not add word to database | See logfile")
		log.write("Encountered exception adding word (" + word + ") to database | Full Exception Code: " + str(e) + '\n')
	cursor.close()	

def connect():
	'''
	Usage: 
			attempts to create wordbank file and table, then connects to the wordbank.db file
	Args:
			none
	Returns:	
			database connection
	'''
	connection = sqlite3.connect("wordbank.db")
	return connection

def add_basic():
	''' 
	Usage: 
			adds basic words to wordbank database
	Args:
			none
	Returns:	
			none, edits database in place
	'''
	basic_words = open("basicWords.txt", "r")
	logfile = open("basic_log.txt", 'w')
	connection = connect()
	try:
		for line in basic_words:
			parts = line.strip().split(",")
			print parts
			add(connection, parts[0], int(parts[1]), logfile)
	except Exception as e:
		logfile.write("error adding basic word")

def test():
	connection = connect()
	test_words = ["and","opposite","animalistic"]
	assert get_syl(connection, test_words[0]) == 1
	assert get_syl(connection, test_words[1]) == 3
	assert get_syl(connection, test_words[2]) == None

if __name__ == "__main__":
	if init() > 0:
		add_basic()
	else:
		test()