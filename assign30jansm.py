#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Q1
"""
marks=int(input("enter percentage marks "))
if marks>90:
    print("Grade= A")
elif 80<marks<=90:
    print("Grade = B")
elif 60<=marks<=80:
    print("Grade =C")
        
else:
    print("Grade=D")


# In[5]:


"""
Q2
"""
cost=int(input("enter cost price of bike  "))
if cost>100000:
    print("Tax = ",cost*0.15)
elif 50000<cost<=100000:
    print("Tax = ",cost*0.10)
        
else:
    print("Tax",cost*0.05)


# In[ ]:


"""
Q3
"""
word=str(input("enter word out of delhi,aagra,jaypur"))
if word=="Delhi":
    print("Red Fort")
elif word=="Aagra":
    print("Taj Mahal")
elif word=="Jaypur":
    print("Jal Mahal")
else:
    print("word out of list")


# In[26]:


"""
Q4

"""
n=3
count=0
if n%3==0:
    while n>10:
        n=n//3
        count+=1
    print(count)
        
if n<10:
    print("no less than 10")
else:
    print("not divisible by 3")


# In[27]:


"""
why and when to use while loop in python give detailed discription with example

Ans:while loop is used when we want to run code untill certain condition is met

"""


# In[32]:


i=1
while i<=9:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1


# In[1]:


i = 10
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i -= 1


# In[ ]:


i = 1
while i <= 5:
    j = 1
    while j <= 5-i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= i:
        print("*", end="")
        k += 1
    print()
    i += 1


# In[ ]:


# reverse while loop to display no form 10 to 1
2+2


# In[ ]:


n=10
while n>=1:
    print(n)
    n=n-1


# In[ ]:




