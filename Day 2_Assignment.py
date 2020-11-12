#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Que.1


# In[28]:


#Create an empty list
list = []


# In[14]:


list = [1,2,3,4,5,6,7,8,9,10]
for num in list:
  if num % 2 == 0:
        print(num, end = " ")


# In[ ]:


#Que.2


# In[41]:


list_1 = [-3,-2,-1,0,1,2,3]
list_2 = [3,4,5,6,7,8]
list_3 = [x * y for x in list_1 for y in list_2 if x > 0 if y % 2 == 0]
print(list_3)


# In[ ]:


#Que.3


# In[49]:


n=int(input("input "))
for n in range(1,15):
    d[n]=n**2
print(d)


# In[ ]:


#Que.4


# In[ ]:


pos = {"x":0, "y":0}
z = int(input())
c=0
while (c!=z):
    n = input()
    c=c+1
    if not n:
        break
        direction,steps=n.split()
        if direction == "UP":
           pos["y"] += int(steps)
        elif direction =="DOWN":
           pos["y"] -= int(steps)
        elif direction =="LEFT":
            pos["x"] -= int(steps)
        elif direction =="RIGHT":
            pos["x"] += int(steps)
        print(int(round((pos["x"]**2 + pos["y"]**2)**0.5)))
                


# In[ ]:




