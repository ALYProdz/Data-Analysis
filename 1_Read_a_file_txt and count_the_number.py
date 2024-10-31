#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Read a file
#Create a function for read a file
def read_a_file(file):
    """This function will read text a file"""
    #First, Open the file as f
    with open(file, "r") as f:
        #Read the file
        f = f.read()
        #Replace the unvwanted character
        f = f.replace("\n","").replace("\r","")
        f = f.lower()
        return f


# In[33]:


v = "./Downloads/prog_1.txt"


# In[34]:


read_a_file(v)


# In[35]:


#Count the number of word in a file
def word_count(file):
    count_word = {}
    for word in file.split(" "):
        if word in count_word:
            count_word[word] +=1
        else:
            count_word[word] = 1
    return count_word


# In[36]:


word_count(read_a_file(v))


# In[ ]:




