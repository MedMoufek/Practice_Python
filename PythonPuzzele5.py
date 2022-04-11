def SubStrTest(my_str_list):
	"""Write a Python program to check the nth-1 string is a proper
	substring of nth string in a given list of strings.
	Exp:
	Input:
	['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
	Output:
	True"""

	n = len(my_str_list)
	return my_str_list[n-2] in my_str_list[n-1]

print(['a', 'abb', 'sfs', 'oo', 'de', 'sfde'],"\n",\
	SubStrTest(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
print(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde'],"\n",\
	SubStrTest(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']))
print(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew'],"\n",\
	SubStrTest(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']))
print(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew'],"\n",\
	SubStrTest(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))

""" Sample solution from w3resource site
def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

Rq : The main difference between my solution and there's is exactly like the
     difference between "is a subset of" nd "is a proper subset of"
     """