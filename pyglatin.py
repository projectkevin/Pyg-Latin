pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = original[0]
if len(original) > 0 and original.isalpha():
	if (first == "a" or first == "e" or first == "i" or first == "o" or first == "u"):
		new_word = original+pyg
		print new_word
	else:
		new_word = original[1:len(original)]+original[0:1]+pyg
		print new_word
else:
	print 'empty'