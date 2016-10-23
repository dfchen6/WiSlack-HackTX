import re

def split_words(s, key_words):
	words = re.findall(r'\S+', s)
	result = []
	for word in words:
		curt = {'val': word, 'is_key': word in key_words}
		result.append(curt)
	for res in result:
		print(res)
	return result
