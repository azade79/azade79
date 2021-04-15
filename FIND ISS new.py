#!/usr/bin/env python
# coding: utf-8

# In[1]:


# project no.1: Find ISS code
import pandas as pd
import plotly.express as px
url='http://api.open-notify.org/iss-now.json'
# This address is from open-notify.org
df=pd.read_json(url)
df


# In[2]:


# the df variable is like a table that is not plotable. we should change it's rows to columns.
df['latitude']=df.loc['latitude','iss_position']
df['longitude']=df.loc['longitude','iss_position']
df.reset_index(inplace=True)


# In[3]:


df


# In[4]:


#now we should eliminate some columns before plotting
df=df.drop(['index','message'],axis=1)
df


# In[5]:


#now we plot it
fig=px.scatter_geo(df,lat='latitude',lon='longitude')
fig.show()


# In[ ]:




