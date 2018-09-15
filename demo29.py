count = 0
avg = 0
total = 0
newlist= []
while True:
	sentance = input('Enter Number or enter DONE to complete :')
	if sentance == 'done':
		break
	else:
		newlist.append(int(sentance)) 
avg = sum(newlist)/len(newlist)
print(avg)
print('Done')