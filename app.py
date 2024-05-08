import streamlit as st
import pandas as pd

# Load dataset
def load_data():
    try:
        return pd.read_csv('data/simple_netflix.csv')
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()

# Load data
df = load_data()

# Check data loading
st.title("Simple Netflix Dashboard")
if not df.empty:
    st.write("### First 5 Records")
    st.write(df.head())
else:
    st.error("Dataset is empty or not loaded correctly.")
