#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("How many figures : ")) 
storage = []
result = []

# Creating an array of users numbers
for i in range(1,num+1):
    a = int(input("Enter value" + str(i) + " : "))
    storage.append(a) # user enter

# Sorting the array
for m in range(len(storage)):
    b = min(storage)
    storage.remove(b)
    result.append(b) # user get
j = ' '.join(str(i) for i in result)
print(j)


# In[ ]:




