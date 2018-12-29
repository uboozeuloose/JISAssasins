#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = []
for i in range(3):
    print("Enter User {} details".format(i))
    acc_no = int(input('Enter Account No: '))
    name = input('Enter Name: ')
    balance = int(input('Enter Balance: '))

    list1.append([acc_no, name, balance])

print("This person has more than 100 rs in their account: \n")

for i in list1:
    if(i[2] > 100):
        print("name = {} and account no = {}".format(i[1], i[0]), end='\n')


# In[ ]:




