# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
with open('/workspaces/semester-1/week1.3/session2/task2/1_word_counter/story.txt', 'r') as f:

    wordcount = 0
    for line in f:
        line = line.replace('\n', '').split(' ')
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings
        line = [cell for cell in line if cell != '']
        wordcount += len(line)
# display the wordcount

print(wordcount)

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210