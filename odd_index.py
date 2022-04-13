def odd(my_str):
	new_str = ""
	for i in range(1,len(my_str),2):
		new_str = new_str + my_str[i]

	return new_str


print(odd("123456789"))