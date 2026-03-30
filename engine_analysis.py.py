#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


data = pd.read_csv("engine_data.csv")
print("Engine Data:")
print(data)


# In[13]:


plt.figure()
plt.plot(data["RPM"], data["Speed"])
plt.title("RPM vs Speed")
plt.xlabel("RPM")
plt.ylabel("Speed")
plt.show()


# In[15]:


plt.figure()
plt.plot(data["RPM"], data["FuelRate"])
plt.title("RPM vs Fuel Rate")
plt.xlabel("RPM")
plt.ylabel("Fuel Rate")
plt.show()


# In[ ]:




