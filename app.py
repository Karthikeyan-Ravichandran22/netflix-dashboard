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

# Load Dataset via file uploader
@st.cache_data
def load_data_via_uploader():
    uploaded_file = st.sidebar.file_uploader("Upload your Netflix CSV file", type=["csv"])
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    else:
        return pd.DataFrame()

# Load Data
df = load_data_via_uploader()

# Sidebar Configuration
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select Page", ["Overview", "Genres", "Countries", "Ratings", "Timeline"])

# Overview Tab
if options == "Overview":
    st.title("📺 Netflix Dashboard Overview")
    st.write("""
        ### Welcome to Netflix Analysis Dashboard!
        Explore various insights into Netflix data with genres, countries, ratings, and more!
    """)
    if not df.empty:
        st.write("### First 5 Records")
        st.write(df.head())
        st.write("### Dataset Summary")
        st.write(df.describe(include='all'))
    else:
        st.warning("Please upload a valid CSV file to get started.")

# Genres Tab
if options == "Genres":
    st.title("🎭 Netflix Genres Analysis")
    if not df.empty:
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
    else:
        st.warning("Please upload a valid CSV file to analyze genres.")

# Countries Tab
if options == "Countries":
    st.title("🌍 Netflix Countries Analysis")
    if not df.empty:
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
    else:
        st.warning("Please upload a valid CSV file to analyze countries.")

# Ratings Tab
if options == "Ratings":
    st.title("⭐ Netflix Ratings Analysis")
    if not df.empty:
        ratings_data = df['rating'].value_counts()

        st.write("### Ratings Distribution")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=ratings_data.index, y=ratings_data.values, ax=ax)
        ax.set_xlabel("Ratings")
        ax.set_ylabel("Count")
        ax.set_title("Ratings Distribution on Netflix")
        st.pyplot(fig)

        st.write("### Dataset by Ratings")
        selected_rating = st.multiselect("Select Rating(s)", ratings_data.index)
        if selected_rating:
            filtered_df = df[df['rating'].isin(selected_rating)]
            st.write(filtered_df)
    else:
        st.warning("Please upload a valid CSV file to analyze ratings.")

# Timeline Tab
if options == "Timeline":
    st.title("🗓️ Netflix Release Timeline Analysis")
    if not df.empty:
        df['release_year'] = pd.to_datetime(df['release_year'], format='%Y', errors='coerce')
        release_timeline = df['release_year'].dt.year.value_counts().sort_index()

        st.write("### Release Timeline Distribution")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(x=release_timeline.index, y=release_timeline.values, ax=ax, marker='o')
        ax.set_xlabel("Release Year")
        ax.set_ylabel("Count")
        ax.set_title("Release Timeline on Netflix")
        st.pyplot(fig)

        st.write("### Dataset by Release Year")
        min_year, max_year = int(df['release_year'].dt.year.min()), int(df['release_year'].dt.year.max())
        selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))
        filtered_df = df[(df['release_year'].dt.year >= selected_year_range[0]) & (df['release_year'].dt.year <= selected_year_range[1])]
        st.write(filtered_df)
    else:
        st.warning("Please upload a valid CSV file to analyze the release timeline.")
