import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv('extensions.csv', delimiter=';')

# Display the logo (optional, remove if not needed)
st.image('logo.png', width=150)

# Title and description
st.title('Name and Extension Search App')
st.write('Search by name or extension to find the corresponding information.')

# Search by name
name_query = st.text_input('🔍 Search by Name')
if name_query:
    name_results = df[df['Name'].str.contains(name_query, case=False, na=False)]
    if not name_results.empty:
        st.write('Results for Name Search:')
        st.dataframe(name_results)
    else:
        st.warning('No results found for that name.')

# Search by extension
extension_query = st.text_input('🔍 Search by Extension')
if extension_query:
    extension_results = df[df['Extension'].astype(str).str.contains(extension_query, case=False, na=False)]
    if not extension_results.empty:
        st.write('Results for Extension Search:')
        st.dataframe(extension_results)
    else:
        st.warning('No results found for that extension.')

