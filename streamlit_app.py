import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import date

# Page title
st.set_page_config(page_title='Volumes Tables', page_icon='📊')
st.title('Volumes Tables')

st.subheader('Historical Volumes')

df = pd.read_csv('data/cum_volume_random.csv')
df.rename(columns={df.columns[0]:"Interval"]}, inplace=True)

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


if genres_selection:
  
  filtered_df = df.drop(columns=genres_selection)
  st.write(filtered_df)
else:
  st.write(df)

#df.year = df.year.astype('int')

# Input widgets
## Genres selection
#genres_list = df.genre.unique()
#genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])

## Year selection
#year_list = df.year.unique()
#year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
#year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

#df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
#reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
#reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# Display DataFrame

#df_editor = st.data_editor(df, height=212, use_container_width=True, num_rows="dynamic")
#df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')


