#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib
matplotlib.__version__


# In[10]:


import matplotlib.pyplot as plt


# In[11]:


import numpy as np


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


x = np.linspace(0,10,100)


# In[15]:


x


# In[16]:


plt.plot(x , np.sin(x), '-')
plt.plot(x , np.cos(x), '--');


# In[17]:


plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');
plt.xlabel('x ekseni')
plt.ylabel('y ekseni')
plt.legend(('sin', 'cos'))


# In[23]:


plt.figure(figsize=(10,4))
plt.subplot(2,1,1)
plt.xlabel('x ekseni')
plt.plot(x, np.sin(x), '-')
plt.ylabel('y ekseni')
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), '--');
plt.xlabel('x ekseni')
plt.ylabel('y ekseni')


# In[25]:



import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


iris = sns.load_dataset('iris')
iris.head()


# In[29]:


iris['petal_length'].plot()


# In[30]:


sns.lineplot(data=iris, y='petal_width', x=iris.index, hue='species')


# In[31]:


fig, ax = plt.subplots() # olası notasyon bu şekildedir.
ax.scatter(iris['sepal_length'], iris['sepal_width'])
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')


# In[32]:


from numpy.random import randn
from matplotlib import pyplot
x = 20 * randn(1000) + 100
y = x + (10 * randn(1000) + 50)
pyplot.scatter(x, y)
pyplot.show()


# In[33]:


iris.groupby(by='species').mean()['petal_length']


# In[34]:


data = iris.groupby(by='species').mean()['petal_length']
ax = sns.barplot(x=data.index, y=data.values)
ax.set_title('Petal Length Means')
ax.set_xlabel('Species')
ax.set_ylabel('Mean')


# In[35]:


iris.corr()


# In[36]:


sns.heatmap(iris.corr())


# In[37]:


sns.heatmap(iris.corr(), annot=True)


# In[38]:


sns.boxplot(y='sepal_length', x='species', data=iris)


# In[ ]:




