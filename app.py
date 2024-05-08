import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Page Configuration
st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="📺",
    layout="wide",
)

# Load dataset via file uploader (outside the cached function)
uploaded_file = st.sidebar.file_uploader("Upload your Netflix CSV file", type=["csv"])

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Load Data
if uploaded_file is not None:
    df = load_data(uploaded_file)
else:
    df = pd.DataFrame()

# Dashboard Layout
st.title("📺 Netflix Dashboard")
st.write("""
    ### Welcome to Netflix Analysis Dashboard!
    Explore various insights into Netflix data with genres, countries, ratings, timeline, and more!
""")

if not df.empty:
    # Overview Section
    st.subheader("Overview")
    st.write("### First 5 Records")
    st.write(df.head())
    st.write("### Dataset Summary")
    st.write(df.describe(include='all'))

    # Genres Section
    st.subheader("🎭 Genres Analysis")
    genre_data = df['listed_in'].str.get_dummies(sep=', ')
    genre_distribution = genre_data.sum().sort_values(ascending=False)

    st.write("### Genre Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=genre_distribution.index, x=genre_distribution.values, ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Genres")
    ax.set_title("Genre Distribution on Netflix")
    st.pyplot(fig)

    st.write("### Dataset by Genre")
    selected_genre = st.multiselect("Select Genre(s)", genre_data.columns)
    if selected_genre:
        filtered_df = df[genre_data[selected_genre].any(axis=1)]
        st.write(filtered_df)

    # Countries Section
    st.subheader("🌍 Countries Analysis")
    country_data = df['country'].str.get_dummies(sep=', ')
    country_distribution = country_data.sum().sort_values(ascending=False).head(15)

    st.write("### Country Distribution (Top 15)")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=country_distribution.index, x=country_distribution.values, ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Countries")
    ax.set_title("Top 15 Countries Producing Netflix Content")
    st.pyplot(fig)

    st.write("### Dataset by Country")
    selected_countries = st.multiselect("Select Country(s)", country_data.columns)
    if selected_countries:
        filtered_df = df[country_data[selected_countries].any(axis=1)]
        st.write(filtered_df)

    # Ratings Section
    st.subheader("⭐ Ratings Analysis")
    ratings_data = df['rating'].value_counts()

    st.write("### Ratings Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=ratings_data.index, y=ratings_data.values, ax=ax)
    ax.set_xlabel("Ratings")
    ax set_ylabel("Count")
    ax set Title
