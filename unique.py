def uni(my_str):
	dictionary = {}
	words = my_str.split(',')

	for word in words:
		if word in dictionary:
			dictionary[word]=+1
		else:
			dictionary[word] = 1

	for i in dictionary:
		if dictionary[i] >1:

		    print(dictionary.pop(word))

	return sorted(dictionary.keys())


print(uni('red,white,black,red,green,black'))

#items = input("Input comma separated sequence of words")
#words = [word for word in items.split(",")]
#print(",".join(sorted(list(set(words)))))