def To(my_list):

	"""Write a Python program find a list of integers with exactly 
	two occurrences of nineteen and at least three occurrences of five.
	Exp: Input:
	[19, 19, 15, 5, 3, 5, 5, 2]
	Output:
	True"""

	nineteen = 0
	five = 0


	for x in my_list:
		if x == 19:
			nineteen = nineteen+1
		elif x == 5:
			five = five+1
		else:
			pass

	if nineteen == 2 and five >= 3:
		print("True")
	else:
		print("False")


print("Expected output: \nTrue\nFalse\nTrue\n")
print("My output:\n")
To([19, 19, 15, 5, 3, 5, 5, 2])
To([19, 15, 15, 5, 3, 3, 5, 2])
To([19, 19, 5, 5, 5, 5, 5])
