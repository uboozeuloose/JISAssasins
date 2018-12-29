#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[4]:


num=input("Enter any four digit number\n")
a=0
b=0
c=0
if (num[0]=='0'):
        num==input("Please enter any other number\n")
for x in num:
        print(int(x))
        if x=='0':
            a=a+1
        elif int(x)%2 == 0:
            b=b+1
        else:
            c=c+1
        

print("even numbers: ",b)
print("odd numbers: ",c)
print("zero: ",a)
    


# In[ ]:




