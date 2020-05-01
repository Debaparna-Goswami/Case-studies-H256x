def read_book(title_path):
    """Read a book as a string. With special characters removed."""
    with open(title_path,"r",encoding="utf8") as current_file:

        text = current_file.read()
        text = text.replace("\n","")
        text = text.replace("\r","")
    return text

text = read_book("/home/debaparna/Documents/Python_for_research/Case studies/Project_Guttenberg_NLP/Books/English/shakespeare/Romeo and Juliet.txt")


i = text.find("What's in a name?")
i

def count_words_fast(text):
    """Returns numbers of occurences of a word in a text."""
    from collections import Counter
    text = text.lower()
    skips = [",",".",":",";","'",'"',"!","-"]
    for ch in skips:
        text.replace(ch,"")
    text = text.replace(".","")
    text = text.split(" ")
    word_counts  = Counter(text)
    return word_counts

def word_stats(text):
    """Returns the number of unique words in a text and the counts of each unique words."""
    return len(count_words_fast(text)),sum(count_words_fast(text).values())



t = word_stats(text)
t


# Comapre this with the book's German transplation.
text_ger = read_book('/home/debaparna/Documents/Python_for_research/Case studies/Project_Guttenberg_NLP/Books/German/shakespeare/Romeo und Julia.txt')

print(word_stats(text_ger))# for German Translation






import os
direct = "/home/debaparna/Documents/Python_for_research/Case studies/Project_Guttenberg_NLP/Books"
os.listdir(direct)



import pandas as pd
stats = pd.DataFrame(columns = ("Language","Author","Title","Length","Unique"))

title_num = 1

for language in os.listdir(direct):
    for author in os.listdir(direct+ "/"+language):
        for title in os.listdir(direct+ "/"+language + "/"+author):
            inputfile = direct+ "/"+language + "/"+author+"/"+title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique,counts) = word_stats(text)
            stats.loc[title_num] = language,author.capitalize(),title.replace(".txt",""),counts,num_unique
            title_num+=1
stats
