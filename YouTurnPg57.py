#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades','BS','MS','PHD'])
df


# In[7]:


df.count()


# In[8]:


df.mean()


# In[9]:


df.std()


# In[10]:


df.min()


# In[11]:


df.max()


# In[13]:


df.quantile(.25)


# In[14]:


df.quantile(.50)


# In[15]:


df.quantile(.75)


# In[ ]:




