#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd


Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[40]:


# Created data manually to load into df and visualizations
Names = ['Jada Walters','Nicole Henderson','Tanya Moore','Ronelle Jackson','Brad Sears']
Gender = ['F','F','F','F','M']
HoursWorked = [39,46,42,38,33]
SalesTraining = ['N','N','Y','Y','N']
YearsExperience = [3,3,4,5,4]
CarsSold = [2,6,6,3,2]
SalesList = zip(Names,CarsSold,Gender)
df = pd.DataFrame(data = SalesList, columns=['Names', 'CarsSold', 'Gender'])

get_ipython().run_line_magic('matplotlib', 'inline')


# In[41]:


# Bar chart
df2 = df.set_index(df['Names'])
df2.plot(kind="bar")


# In[49]:


# Box chart
axis1 = df.boxplot(by='Gender', column='CarsSold')
axis1.set_ylim(0,8)


# In[ ]:




