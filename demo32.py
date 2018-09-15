fhand = open('testfile.txt')
count = 0
# count the number of the lines in the file
for line in fhand:
	count = count + 1
print(count)