#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Que.1
#importing numpy
import numpy as np


# In[2]:


np.arange(2,50,3)


# In[3]:


#Que.2
list1 = np.array([0,1,2,3,4])
list2 = np.array([5,6,7,8,9])

arr = np.concatenate((list1,list2))
print(arr)


# In[7]:


#Que.3
a = np.array([[3,4],[0,2]])
a.shape   #both the first and second axis have 2( columns/rows)data


# In[8]:


#num of dimensions
a.ndim


# In[13]:


#Que.4
arr = np.array([1,2,3,4,5,6])
arr_2d = np.reshape(arr, (2,3))
print(arr_2d)


# In[14]:


#Que.5
a = np.array([[0,1],[2,3]])
b = np.array([[4,5],[6,7]])
#vertical stacking
print("Vertical stacking:\n", np.vstack((a,b)))


# In[15]:


#horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a,b)))


# In[16]:


#Que.6
list = [0,1,1,3,5,4,9,6,2]
#converting our list to set
new_set = set(list)
print(len(new_set))


# In[20]:





# In[ ]:




