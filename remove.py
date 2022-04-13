def remove_nth_char(string, n):
	new_string = ""
	for i in range(len(string)):
		if i != n-1:
			new_string = new_string + string[i]

	return new_string

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part


print(remove_char('Python', 3))
print(remove_nth_char("Exercises", 4))
