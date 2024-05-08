import streamlit as st
import pandas as pd

<<<<<<< HEAD
# Load dataset using file uploader
def load_data_via_uploader():
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    else:
=======
# Load dataset
def load_data():
    try:
        return pd.read_csv(r'data/simple_netflix.csv')
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
>>>>>>> 724c6ddc5747acc207e90e0cb21a0941f9c7d462
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
