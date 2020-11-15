#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Que.1
#importing pandas and checking version
import pandas as pd
print(pd.__version__)


# In[2]:


#Que.2
#importing numpy
import numpy as np
input = np.array(['a','b','c','d','e','f'])   #numpy array
s = pd.Series(input)     #creating series
print(s)


# In[6]:


#Que.3
#creating the dataframe df
df = pd.DataFrame({'Roll Number': ['5SSC23','5SSC33','5SSC42','5SSC50','5SSC60'],
                  'Name': ['Mona','Shruti','Tushar','Ashish','Ritu'],
                  'Subject': ['Mathematics','Mathematics','Mathematics','Mathematics','Mathematics'],
                  'Grade': ['A','B','B','A','C'],
                  'Marks In Percentage': [83,73,75,92,59]})
#printing df
df


# In[7]:


#Que.4
#importing seaborn
import seaborn as sns
mpg = sns.load_dataset('mpg')


# In[8]:


mpg.head()


# In[9]:


mpg.shape


# In[ ]:


#Que.5
Ans:usa

