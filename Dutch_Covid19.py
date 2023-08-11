#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# In[29]:


df = pd.read_csv('DutchData_Dashboard.csv')
df = df.groupby('Province')['Total_reported'].mean()
df = df.reset_index()
fig = plt.figure(figsize = (19, 10))

plt.bar(df['Province'], df['Total_reported'], color = 'maroon')
plt.xlabel('Province')
plt.ylabel('Reported COVID-19 cases')
plt.title('Provinces in the Netherlands \ Number of Reported COVID-19 cases')
pro = df['Province'].unique().tolist()
province_list = st.multiselect('Choose Province:',options = pro)


#displaying the selected options

st.write('You have selected:', province_list)
st.pyplot(fig)

