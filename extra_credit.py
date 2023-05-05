#please complete the following exercises using Dictionaries

#Word Index - Analyze the text of the book of John from the Bible 
#and display how many times each of these words show up in the text 
#- 'Father', 'God', 'Christ', 'Spirit', 'life', 'man' (case sensitive). 
#The text file is available here (note: all punctuation marks, chapter and verse references have been removed to allow to analyze each word) - 

infile = open('BookJohn.txt', 'r')
john = infile.read()
words_to_count = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man']

word_counts = {word: john.count(word) for word in words_to_count}

for word, count in word_counts.items():
    print(word, count)
