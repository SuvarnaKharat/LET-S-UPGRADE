#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=("LETS UPGRADE")
print(a)


# # To Calculate profit and Loss(Que.3)

# In[11]:


cost_price = float(input('cost_price:'))
selling_price = float(input('selling_price:')) 
if (selling_price > cost_price):
    Profit = selling_price - cost_price
    print('Profit=',Profit)
elif (selling_price < cost_price):
    Loss = Cost_price - selling_price
    print('Loss',Loss)
else:
    print('Neither')


# # Currency Conversion(Que.4)

# In[2]:


Rupees = float(input())
Euro = Rupees * 80
print(Euro)


# In[ ]:




