import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import date

# Page title
st.set_page_config(page_title='Volumes Tables', page_icon='📊')
st.title('Volumes Tables')

st.subheader('Historical Volumes')

col1, col2, col3 = st.columns(3)

with col1:
  options = ["Option 1", "Option 2", "Option 3"]
  selected_option = st.selectbox("Select and option:", options)
with col2:
  selected_date = st.date_input("Select a date:", value=date.today())
with col3:
  radio_options = ["Choice 1", "Choice 2", "Choice 3"]
  selected_radio = st.radio("Select one:", radio_options)

# Load data
#path = 
df = pd.read_csv('data/movies_genres_summary.csv')
df.year = df.year.astype('int')

# Input widgets
## Genres selection
genres_list = df.genre.unique()
genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])

## Year selection
year_list = df.year.unique()
year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# Display DataFrame

df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
                            column_config={"year": st.column_config.TextColumn("Year")},
                            num_rows="dynamic")
df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

# Display chart
chart = alt.Chart(df_chart).mark_line().encode(
            x=alt.X('year:N', title='Year'),
            y=alt.Y('gross:Q', title='Gross earnings ($)'),
            color='genre:N'
            ).properties(height=320)
st.altair_chart(chart, use_container_width=True)
