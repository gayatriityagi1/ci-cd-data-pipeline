import streamlit as st
import sqlite3
import pandas as pd

st.title("CI/CD Data Pipeline Dashboard")

conn = sqlite3.connect('db/pipeline.db')
df = pd.read_sql("SELECT * FROM clean_data", conn)
conn.close()

st.metric("Total Records", len(df))
st.dataframe(df.head())
