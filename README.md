# syllagetter

## Overview
Accesses Merriam Webster Dictionary API to determine number of syllables in a word.

### General Flow
- get body of text
- cycle through body of text creating a dictionary of words and occurences
- check database for each word in dictionary
	- if found, 
		- add (syllables * occurences) to total syllable count.
	- else, 
		- add to dict of words to be looked up
- use Merriam Webster Dictionary API to lookup remaining words.
	- start with learning dictionary
		- if found, 
			- add (syllables *occurences) to total syllable account
			- add word, syllable count to database
		- else,
			- try again with collegiete dictionary
				- if found, 
					- add (syllables *occurences) to total syllable account
					- add word,syllable to database
				- else,
					- log unfindable word and number of occurences
	- if over request limit, switch to collegiete dictionary
		- if found, 
			- add (syllables *occurences) to total syllable account
			- add word, syllable count to database
		- else,
			- log unfindable word and number of occurences
return syllable count