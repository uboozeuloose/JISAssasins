#!/usr/bin/env python
# coding: utf-8

# In[2]:



num=input("Enter any four digit number\n")
a=0
b=0
c=0
if (num[0]=='0'):
        num==input("Please enter any other number\n")
for x in num:
    if int(x)%2 == 0:
        a=a+1
    elif x == 0:
        b=b+1
    else:
        c=c+1
        

print("even numbers: ",a)
print(" odd numbers: ",c)
print(" zero: ",b)
    


# In[ ]:





# In[ ]:




