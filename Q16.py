#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Letr:
    def Ascii(self,c):
        
        y=ord(c)
        nex=chr(ord(c)+1)
        pre=chr(ord(c)-1)
        print("{}={} next letter={} prev letter ={}".format(c,y,nex,pre))
l=Letr()
c=input("enter c\t")
l.Ascii(c)

