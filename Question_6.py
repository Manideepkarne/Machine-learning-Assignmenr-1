string = "I am a teacher and I love to inspire and teach people"
words = string .split() #spliting string into list of words
set_words = set(words) #allocating list into a set
print("number of unique words;", len(set_words)) #number of unique words is printed
print("unique words:",set_words) #printing unique words in the set