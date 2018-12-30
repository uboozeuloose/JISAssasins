#!/usr/bin/env python
# coding: utf-8

# In[1]:


basic_salary = int(input("enter the salary:"))
gross_salary = 0

if basic_salary >= 5000:
    hra = (15/100)*basic_salary
    da = (150/100)*basic_salary
elif basic_salary < 5000:
    hra = (10/100)*basic_salary
    da = (110/150)*basic_salary
gross_salary=basic_salary+hra+da
print("gross_salary is = ", gross_salary)
    


# In[ ]:




