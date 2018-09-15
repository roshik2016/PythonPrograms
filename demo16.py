numbers=[30,5,12,20,25,7,8,9]
small = numbers[0]
for n in numbers:
	if n<small:
		small = n 
print(small)