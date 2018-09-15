count = 0
avg = 0
total = 0
while True:
	sentance = input('Enter Number or enter DONE to complete :')
	if sentance == 'done':
		break
	else:
		count = count+1
		total = total+sentance 
		avg = total/count
print(count)
print(int(total))
print(avg)
print('Done')