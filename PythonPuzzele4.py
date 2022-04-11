def Piles(n):
	"""we are making n stone piles!
	If n is even, then all piles have an even number of stones.
	If n is odd, all piles have an odd number of stones.
	Each pile must Have more stones than the previous pile but as 
	few as possible. Write a Python program to find the number 
	of stones in each pile.
	Exp: 
	Input: 2
	Output:[2, 4]
	"""

	result = list()
	for i in range(n%2,n*2+1,2):
		result.append(i)

	if 0 in result:
		result.remove(0)

	return result

print(Piles(1))
print(Piles(2))
print(Piles(3))
print(Piles(4))
print(Piles(5))