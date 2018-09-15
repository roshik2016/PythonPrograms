import sys

fhand = input("Enter the name of the file")
fp = open(fhand)
data = fp.read()
words = data.split()
fp.close()
unwanted_char = "?,.!"

wordfreq = {}
for each_word in words:
	each_word = each_word.strip(unwanted_char)
	if each_word not in wordfreq:
		wordfreq[each_word] = 0 
	wordfreq[each_word] += 1
print(wordfreq)