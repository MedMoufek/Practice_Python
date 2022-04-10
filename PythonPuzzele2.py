def Co(my_list):
	""" Write a Python program that accept a list of integers 
	and check the length and the fifth element. Return true if the 
	length of the list is 8 and fifth element occurs thrice in the 
	said list.

	Exp:
	Input:
	[19, 19, 15, 5, 5, 5, 1, 2]
	Output:
	True """

	if len(my_list) == 8 and my_list.count(my_list[4]) == 3:
		print("True")
	else:
		print("false")


print("Expected Outputs:\nTrue\nFalse\nTrue\nFalse\n")
print("My program output is:")
Co([19, 19, 15, 5, 5, 5, 1, 2])
Co([19, 15, 5, 7, 5, 5, 2])
Co([11, 12, 14, 13, 14, 13, 15, 14])
Co([19, 15, 11, 7, 5, 6, 2])