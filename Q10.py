#!/usr/bin/env python
# coding: utf-8

# In[2]:


def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 
              
   
    print(string) 
  
 
string = "happy birthday"
rem_vowel(string) 


# In[ ]:




