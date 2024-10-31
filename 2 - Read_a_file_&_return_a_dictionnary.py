#!/usr/bin/env python
# coding: utf-8

# In[48]:


# Function to file the dictionary

def read_dictionary(file_path):
    """This function will read a file and return it as a dictionnary"""
    original_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            # Handling multiple values for each key
            values = value.split(', ')
            original_dict[key] = values if len(values) > 1 else value
    return original_dict


# Function to invert the dictionary

def invert_dictionary(dictionary):
    """This function will invert a dictionnary"""
    inverted_dict = {}
    for key, values in dictionary.items():
        # If the value is a list (i.e., multiple values for a single key), iterate over each
        if isinstance(values, list):
            for value in values:
                inverted_dict.setdefault(value, []).append(key)
        else:
            # Otherwise, it's a single value
            inverted_dict.setdefault(values, []).append(key)
    return inverted_dict


# In[55]:


#Read the file
open("./Downloads/Input_dict5.txt", "r").read()


# In[58]:


#Read the file and return a dictionnary
read_dictionary("./Downloads/Input_dict5.txt")


# In[59]:


#Invert a dictionnary
invert_dictionary(read_dictionary("./Downloads/Input_dict5.txt"))


# In[ ]:




