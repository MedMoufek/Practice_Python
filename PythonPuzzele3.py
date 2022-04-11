def Gm(i):
	"""Write a Python program that accept an integer test whether
	an integer greater than 4^4 and which is 4 mod 34.

	Exp:
	Input:
	922
	Output:
	True"""

	return i>=4^4 and i%34==4

print("Expected Outputs:\nTrue\nFalse\nTrue\n")
print("My program output is:")
print(Gm(922))
print(Gm(914))
print(Gm(854))