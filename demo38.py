fname=input('Enter the name of the file')
try:
	fhand = open(fname)
except:
	print("file not found",fname)
	exit()
count = 0
# coun the number of lines that starts with "Subject:
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print(count)