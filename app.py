import streamlit as st
import pandas as pd

# Load dataset using file uploader
def load_data_via_uploader():
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    else:
        return pd.DataFrame()

# Load data
df = load_data_via_uploader()

# Check data loading
st.title("Simple Netflix Dashboard")
if not df.empty:
    st.write("### First 5 Records")
    st.write(df.head())
else:
    st.error("Please upload a valid CSV file.")
