from collections import Counter
fname = input("enter name of the file")
fhand = open(fname)
data = fhand.read()
words = data.split()
count = dict(Counter(words))
print(count)