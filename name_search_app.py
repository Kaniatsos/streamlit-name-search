import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv('extensions.csv', delimiter=';')

# Display the logo
st.image('logo.png', width=150)

# Title and description
st.title('UnipakHellas Extension Search App')
st.write('Enter a name to search for its corresponding extension.')

# Search box
search_query = st.text_input('Search for a name')

# Filter the dataframe based on the search query
if search_query:
    results = df[df['Name'].str.contains(search_query, case=False, na=False)]
    if not results.empty:
        st.write('Search Results:')
        st.dataframe(results)
    else:
        st.write('No results found.')
