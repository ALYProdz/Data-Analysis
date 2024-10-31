#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
        return f


# In[7]:


v = "./Downloads/prog_1.txt"


# In[8]:


read_a_file(v)


# In[ ]:




