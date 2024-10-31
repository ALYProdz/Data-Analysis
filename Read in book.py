#!/usr/bin/env python
# coding: utf-8

# <h2>Read in a book</h2>

# <p><h3>In this case study, we're going to read some book from the project Gutenberg, and we gonna make the statistics to find how many word is appear in each book</h3></p>

# In[43]:


#Let's import some importants module
from collections import Counter
import scipy as ss
from scipy.stats import mstats
import matplotlib.pyplot as plt


# In[44]:


#Let's define a function to read all the book 
def read_book(title_path):
    """This function goin to rea a book and return a string special
    Let open the file as current_file
    with the with open statement
    """
    with open(title_path, "r", encoding="utf-8") as current_file:
        """Let capture the value like a text and read the file with the read() attributes"""
        text = current_file.read()
        """Let's replace all the characters and unknown"""
        text = text.replace("\n", "").replace('\r',"")
        skip = [",", ".", "'", '"', "-", ";", ":"]
        for ch in skip:
            text.replace(ch, "")
    return text


# In[45]:


#Let's read the Romeo_and_Juliet in English and German
Romeo_and_Juliet_Eng = read_book(".\\Downloads\\Book\\Books_EngFr\\Books_EngFr\\English\\shakespeare\\Romeo and Juliet.txt")
Romeo_und_julia_Germ = read_book(".\\Downloads\\Book\\Books_GerPort\\Books_GerPort\\German\\shakespeare\\Romeo und Julia.txt")


# In[46]:


#Let's see the length of eachh one in a tupple.
len(Romeo_and_Juliet_Eng), len(Romeo_und_julia_Germ)


# In[47]:


#There is a good part in the book, let's find it.
Ind = Romeo_and_Juliet_Eng.find("What's in a name?")
Ind


# In[48]:


read_sample_text = Romeo_and_Juliet_Eng[Ind : Ind + 10000] 
len(read_sample_text)


# In[49]:


read_sample_text


# In[50]:


other=Romeo_and_Juliet_Eng.find("Thou mayst prove false.")
other


# In[51]:


autre = Romeo_and_Juliet_Eng[other : other + 100]
autre


# <h1>Statistics</h1>

# <h3>In this case study,we're goind to find the statistics of a book, find the word count</h3>

# In[52]:


#Let's define a function to count the word in a book.
def count_words(Romeo_and_Juliet_Eng):
    """This function will count the word of a book"""
    #First, lets turn the book into lower case and replace all the special character
    Romeo_and_Juliet_Eng = Romeo_and_Juliet_Eng.lower()
    skip = [",", ".", "'", '"', "-", ";", ":"]
    for ch in skip:
        Romeo_and_Juliet_Eng.replace(ch, "")
    words_count = Counter(Romeo_and_Juliet_Eng.split(" "))
    return words_count


# In[53]:


words_count = count_words(Romeo_and_Juliet_Eng)


# In[54]:


#Length of words_count
len(words_count)


# In[55]:


words_count


# In[56]:


sum(words_count.values())


# In[57]:


#Let's create the statistic of the book
#Let's create a function for the statistic
def word_stats(words_count):
    """THis functionn will make the statistics of the book"""
    #Find the number of unique word.
    num_unique = len(words_count)
    counts = words_count.values()
    return (num_unique, counts)


# In[58]:


#Let's capture it
num_unique, counts = word_stats(words_count)


# In[59]:


num_unique
print(f"There is {num_unique} unique words.")


# In[60]:


words_count = count_words(Romeo_and_Juliet_Eng)
num_unique, counts= word_stats(words_count)


# In[ ]:





# In[61]:


#Let's print the number of unique words here
print("There is in total", num_unique, "unique words in the book Romeo and Juliet in English version.")


# In[ ]:





# In[62]:


#Let's print the sum of the word
print("There is in total", sum(counts), "words in the book Romeo and Juliet in english")


# In[ ]:





# In[ ]:





# In[63]:


words_count = count_words(Romeo_und_julia_Germ )
num_unique, counts= word_stats(words_count)


# In[64]:


#Let's print the number of unique words here
print("There is in total", num_unique, "unique words in the book Romeo and Juliet in German version.")


# In[65]:


#Let's print the sum of the word
print("There is in total", sum(counts), "words in the book Romeo and Juliet in German version")


# In[ ]:





# In[66]:


#Let's print the number of unique words here.
print(f"There is in total {num_unique} unique words in the book Romeo and Juliet  German version, and a total of {sum(counts)} of words.")


# In[ ]:




