#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('DutchData_Dashboard.csv')
df = df.groupby('Province')['Total_reported'].mean()
df = df.reset_index()

pro = df['Province'].unique().tolist()
province_list = st.multiselect('Choose Province:',options = pro)

#displaying the selected options

st.write(province_list)
if not province_list:
    filtered_data = df.copy()
else:
    filtered_data = df.loc[df["Province"].isin(province_list)]

# st.dataframe(filtered_data, width=1000, height=500) if you want to see the dataframe just add this.

# Only the filtered data is used below.

fig = plt.figure(figsize = (19, 10))

plt.bar(filtered_data['Province'], filtered_data['Total_reported'], color = 'maroon')
plt.xlabel('Province')
plt.ylabel('Average count of COVID-19 cases')
plt.title('Provinces in the Netherlands \ Average Count of the Reported COVID-19 cases')

st.pyplot(fig)

