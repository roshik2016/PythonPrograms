from collections import Counter
fname = input("enter name of the file")
fhand = open(fname)
data = fhand.read()
words = data.split()
unwanted_char = "?,.!"
words = [new_words.strip(unwanted_char) for new_words in words]
count = dict(Counter(words))
print(count)