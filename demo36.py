fhand = open('testfile.txt')
for line in fhand:
	line = line.rstrip() # this removes the empty lines in the file.
	if line.find('@uct.ac.za')== -1:
		continue
	print(line)