def split_words(s, key_words):
	classified = {}
	check = []
	for i in range(0, len(s)):
		check.append(0)
	for word in key_words:
		start = s.find(word)
		end = start + len(word) - 1
		check[start] = 1
		check[end] = 1
	# Iterate from beginning and gather intervals
	p = 0
	is_key = []
	marked_words = []
	slow = 0
	key_word = False
	while p < len(s):
		while p < len(s) and check[p] == 0:
			p = p + 1
		if p == 0:
			p = p + 1;
			key_word = True
			continue
		part = s[slow : p : 1]
		
		marked_words.append(part)
		is_key.append(key_word)
		slow = p
		key_word = not key_word
		p = p + 1
	for each_part in marked_words:
		print(each_part)

if __name__ == "__main__":
    split_words("today he went to japan and france", {'japan', 'and'})