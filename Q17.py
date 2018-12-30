#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Number: 
    def __init__(self,array):
        self.array = array
    def fun(self):
        n=int(input("Enter how many: "))
        self.array=[]
        for i in range(n):
            num=int(input("Enter a number: "))
            (self.array).append(num)
        print("The array is= " , self.array)
    def sorting(self):
        (self.array).sort()
        print("The array after sort is= " , self.array)
ob = Number(1)
ob.fun()
ob.sorting()


# In[ ]:




