def test(my_list):
	"""Write a Python program to check a given list of integers where
	 the sum of the first i integers is i.
	 Exp:
	 Input:
	 [0, 1, 2, 3, 4, 5]
	 Output:
	 False"""

	return sum(my_list) == len(my_list)

print(test([0, 1, 2, 3, 4, 5]))
print(test([1, 1, 1, 1, 1, 1]))
print(test([2, 2, 2, 2, 2]))

