import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import date
import seaborn as sns



# Page title
st.set_page_config(page_title='Volumes Tables', page_icon='📊')
st.title('Volumes Tables')

st.subheader('Historical Volumes')

#Read CSV from hub
df = pd.read_csv('data/cum_volume_random.csv')
df.rename(columns={df.columns[0]:"Interval"}, inplace=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
  options = ["Cumulative Volumes", "Standard Deviation", "% vs Average", "DV01 vs average"]
  selected_option = st.selectbox("Select a feature:", options)
with col2:
  selected_date = st.date_input("Select a date:", value=date.today())
with col3:
  radio_options = ["5 Minutes", "10 Minutes", "15 Minutes"]
  selected_radio = st.radio("Select interval:", radio_options)
with col4: 
  slider_values = [5, 10, 15, 20, 30, 40, 50]
  slider = st.select_slider("Select Average period:", options=slider_values, value=slider_values[0])

future_list = df.columns.tolist()
genres_selection = st.multiselect('Exclude Future', future_list)

cm = sns.light_palette('blue', as_cmap=True)

if genres_selection:
  
  filtered_df = df.drop(columns=genres_selection)
  st.write(filtered_df.style.background_gradient(cmap=cm))
else:
  st.write(df)




