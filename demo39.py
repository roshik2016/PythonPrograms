fout = open('empty.txt','w')
fout.write("this is a new file")

line2 = "\nthis is line 2"
fout.write(line2)

fout.close()