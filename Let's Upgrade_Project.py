#!/usr/bin/env python
# coding: utf-8

# In[9]:


#importing all required packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


PUBG = pd.read_csv('C:\\Users\\mona\\Desktop\\DATA SCIENCE\\ASSIGNMENTS\\Lets upgrade\\pubg.csv')


# In[4]:


PUBG.head()


# In[5]:


PUBG.shape


# In[6]:


PUBG.info()


# In[7]:


PUBG.describe()


# In[8]:


print(PUBG.describe())


# In[11]:


sns.scatterplot(x = 'matchDuration', y = 'walkDistance', data = PUBG)


# In[12]:


#plotting boxplot
sns.boxplot(x='matchType',y='winPlacePerc',data=PUBG)


# In[13]:


sns.boxplot(x='matchType',y='matchDuration',data=PUBG)


# In[26]:


#plotting barplot
sns.barplot(x='matchType',y='killPoints',data=PUBG)


# In[28]:


sns.barplot(x='matchType',y='weaponsAcquired',data=PUBG)


# In[30]:


#plotting pairplot
sns.pairplot(PUBG)


# In[27]:


PUBG._get_numeric_data()


# In[22]:


#finding categorical column
PUBG.select_dtypes(exclude=['int','float']).columns


# In[23]:


#Roundoff column
PUBG['winPlacePerc'].round(decimals=2)


# In[ ]:




