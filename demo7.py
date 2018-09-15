hours = int(input('Enter Number of hours'))
rate_Pay = float(input(' Enter rate of pay'))
if hours>=40:
	print('Your pay is :',hours*rate_Pay*1.5)
else: 
	print('Your Pay is:',hours*rate_Pay)
