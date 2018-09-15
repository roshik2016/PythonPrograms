fhand = open('testfile.txt')
for line in fhand:
	line = line.rstrip() # this removes the empty lines in the file.
	if line.startswith('From:'): # finds all the lines that starts with From:
		print(line)