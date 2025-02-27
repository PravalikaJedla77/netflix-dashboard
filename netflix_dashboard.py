import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Netflix Data Analysis Dashboard")

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Display the dataset
st.write("### Netflix Dataset Preview")
st.dataframe(df.head())

# Show data summary
st.write("### Dataset Summary")
st.write(df.describe())

# Data visualization: Distribution of content types
st.write("### Content Type Distribution")
fig, ax = plt.subplots()
sns.countplot(x="type", data=df, ax=ax)
st.pyplot(fig)

# Data visualization: Top 10 countries with most content
st.write("### Top 10 Countries with Most Content")
top_countries = df['country'].value_counts().head(10)
fig, ax = plt.subplots()
top_countries.plot(kind='bar', ax=ax)
st.pyplot(fig)

# Data visualization: Year-wise content production
st.write("### Year-wise Content Production")
fig, ax = plt.subplots()
sns.histplot(df['release_year'], bins=20, kde=True, ax=ax)
st.pyplot(fig)