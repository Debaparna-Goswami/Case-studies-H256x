#!/usr/bin/env python
# coding: utf-8
# In[12]:

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





sample_text = text[i:i+100]





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








def count_words(text):
    """Returns numbers of occurences of a word in a text."""
    text = text.lower()
    text = text.replace(".","")

    skips = [",",".",":",";","'",'"',"!","-"]
    for ch in skips:
        text.replace(ch,"")
    text = text.split(" ")
    words = {}
    for char in text:
        if char not in words:
            words[char]=text.count(char)
    return words


# In[9]:


t = word_stats(text)
t


# Comapre this with thte book's German transplation.

# In[11]:


text_ger = read_book('/home/debaparna/Documents/Python_for_research/Case studies/Project_Guttenberg_NLP/Books/German/shakespeare/Romeo und Julia.txt')





len(text_ger)




print(word_stats(text_ger))# for German Translation





import os
get_ipython().run_line_magic('pinfo', 'os.listdir')





direct = "/home/debaparna/Documents/Python_for_research/Case studies/Project_Guttenberg_NLP/Books"





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






stats.head(20)




# table = pd.DataFrame(columns=("name","age"))

#
# table

#
# table.loc[0]= "me",22
# table.loc[1]="her",23

# table

#
# for i in range(2,5):
#     table.loc[i] = input(),input()
#     table.loc[i] = input(),input()
#     i+=1

# table

## Plotting Word Statistics
