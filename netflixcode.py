# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12sPudmM7bgae54sBsO1r5ShnNHhM0ZtR
"""

import numpy as np #linear algebra operations
import pandas as pd #used for data preperation
import plotly.express as px #used for data visualization
from textblob import TextBlob #used for sentimental analysis

import os
print(os.getcwd())  # Prints the current working directory

import os

file_path = r'C:\Users\chran\Desktop\pravalika\netflix_titles.csv'  # Ensure correct path

print("Checking if file exists:", os.path.exists(file_path))  # Should return True

print(os.path.expanduser("~"))  # Should return C:\Users\YourCorrectUsername

file_path = r'C:\Users\chran\Desktop\pravalika\netflix_titles.csv'
print(os.path.exists(file_path))  # Should return True

import os
print(os.path.expanduser("~"))  # This will show your correct user folder

from google.colab import files
uploaded = files.upload()  # Upload 'netflix_titles.csv' from your PC

"""# New Section"""

import os
print(os.listdir())  # See available files in the current directory



# Commented out IPython magic to ensure Python compatibility.
# %%writefile netflix_dashboard.py
# print("Hello, this is my new Python file!")
#

import pandas as pd

df = pd.read_csv('netflix_titles.csv', encoding='latin1')
print(df.head())  # Display first few rows

df = df.dropna(axis=1, how='all')  # Removes empty columns
print(df.head())  # Check cleaned data

print(df.isnull().sum())  # Count missing values per column

df = df.fillna('Unknown')  # Replace NaN with 'Unknown'

print(df.info())  # Check data types and column info
print(df.describe())  # Get statistical summary (for numeric columns)
print(df['type'].value_counts())  # Count number of Movies & TV Shows

movies_df = df[df['type'] == 'Movie']
print(movies_df.head())  # Show first 5 movies

tv_shows_df = df[df['type'] == 'TV Show']
print(tv_shows_df.head())  # Show first 5 TV Shows

import matplotlib.pyplot as plt

df['type'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.title('Distribution of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

from textblob import TextBlob

# Function to analyze sentiment
def get_sentiment(title):
    return TextBlob(title).sentiment.polarity  # Returns sentiment score (-1 to 1)

df['sentiment_score'] = df['title'].apply(get_sentiment)
print(df[['title', 'sentiment_score']].head())  # Show sentiment scores

df.to_csv('cleaned_netflix_titles.csv', index=False)
print("Cleaned dataset saved successfully!")

for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

df = df.dropna(axis=1, how='all')

from collections import Counter

# Split genres and count occurrences
all_genres = ', '.join(df['listed_in'].dropna()).split(', ')
genre_counts = Counter(all_genres)

# Convert to DataFrame
genre_df = pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False)
print(genre_df.head(10))  # Show top 10 genres

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.bar(genre_df['Genre'][:10], genre_df['Count'][:10], color='skyblue')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Top 10 Most Common Genres on Netflix')
plt.xticks(rotation=45)
plt.show()

df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
df['release_year'].value_counts().sort_index().plot(kind='line', figsize=(12,6), color='red')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.title('Number of Shows/Movies Released Per Year')
plt.grid()
plt.show()

directors = df['director'].dropna().str.split(', ').explode()
top_directors = directors.value_counts().head(10)
print(top_directors)

actors = df['cast'].dropna().str.split(', ').explode()
top_actors = actors.value_counts().head(10)
print(top_actors)

from wordcloud import WordCloud

text = ' '.join(df['title'])
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Netflix Titles')
plt.show()

import seaborn as sns

plt.figure(figsize=(10, 5))
sns.histplot(df['sentiment_score'], bins=30, kde=True, color='purple')
plt.xlabel('Sentiment Score')
plt.ylabel('Count')
plt.title('Sentiment Analysis of Netflix Titles')
plt.grid()
plt.show()

def recommend_movies(genre, num=5):
    recommendations = df[df['listed_in'].str.contains(genre, na=False)].sample(num)
    return recommendations[['title', 'type', 'listed_in']]

print(recommend_movies('Drama'))  # Recommend 5 random Drama titles

df.to_csv('cleaned_netflix_data.csv', index=False)
print("Cleaned dataset saved successfully!")

print(df.info())  # Data types & missing values
print(df.describe())  # Statistics (only for numerical columns)
print(df.nunique())  # Count of unique values per column

import matplotlib.pyplot as plt

df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
df['release_year'].value_counts().sort_index().plot(kind='line', figsize=(12,6), color='red')

plt.xlabel('Year')
plt.ylabel('Number of Movies & TV Shows')
plt.title('Number of Netflix Releases Per Year')
plt.grid()
plt.show()



# Commented out IPython magic to ensure Python compatibility.
# %%writefile netflix_dashboard.py
# print("Hello, this is my new Python file!")
#

!cat netflix_dashboard.py

!ls  # List files to confirm upload

!ls -l

# Commented out IPython magic to ensure Python compatibility.
# %%writefile netflix_dashboard.py
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# st.title("📊 Netflix Data Analysis Dashboard")
#

!ls -l

from google.colab import files
files.download("netflix_dashboard.py")

from google.colab import drive
drive.mount('/content/drive')

with open('/content/drive/My Drive/netflix_dashboard.py', 'w') as f:
    f.write("# Your Python script content here")

from google.colab import files
files.download('netflix_dashboard.py')

!apt-get install git

!git clone https://github.com/your-username/your-repo.git

!mv netflix_dashboard.py your-repo/

!git clone https://github.com/PravalikaJedla77/netflix-dashboard.git

# Commented out IPython magic to ensure Python compatibility.
# %cd netflix-dashboard

!git clone https://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@github.com/PravalikaJedla77/netflix-dashboard.git

!git clone https://github.com/PravalikaJedla77/netflix-dashboard.git

from google.colab import files
files.download("netflix_dashboard.py")

code = """
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
"""

with open("netflix_dashboard.py", "w") as f:
    f.write(code)

print("File saved successfully!")

!cat netflix_dashboard.py

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/PravalikaJedla77/netflix-dashboard.git
# %cd netflix-dashboard
!mv /content/netflix_dashboard.py .
!git add netflix_dashboard.py
!git commit -m "Updated Netflix dashboard with full analysis"
!git push origin main

!git config --global user.email "pravalikajedla@gmail.com"
!git config --global user.name "PravalikaJedla77"

!rm -rf netflix-dashboard

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/PravalikaJedla77/netflix-dashboard.git
# %cd netflix-dashboard

!git remote set-url origin https://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@github.com/PravalikaJedla77/netflix-dashboard.git
!git add netflix_dashboard.py
!git commit -m "Updated Netflix dashboard with full analysis"
!git push origin main

!pip install streamlit

import streamlit as st
print("Streamlit installed successfully!")

import matplotlib.pyplot as plt

# Example: Save a graph
plt.figure(figsize=(8, 6))
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])  # Example plot
plt.title("Sample Graph")
plt.savefig("sample_graph.png")  # Save the graph
plt.show()

import os
print(os.listdir())  # This will list all files in the current working directory

import os
print(os.listdir())  # This will list all files in the current working directory

import os
print(os.listdir())  # Check if the file is now listed

!find / -name "netflix_titles.csv" 2>/dev/null

import pandas as pd

df = pd.read_csv("/content/sample_data/netflix_titles.csv", encoding="latin1")  # Try 'latin1' or 'ISO-8859-1'
df.head()

df = pd.read_csv("/content/sample_data/netflix_titles.csv", encoding="ISO-8859-1")

# Check the first few rows
df.head()

# Get dataset information
df.info()

# Check for missing values
df.isnull().sum()

# Summary statistics
df.describe(include="all")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="type", palette="coolwarm")
plt.title("Count of Movies vs TV Shows")
plt.show()

df["release_year"] = pd.to_datetime(df["release_year"], errors="coerce")
df["release_year"].value_counts().sort_index().plot(kind="line", figsize=(10, 5), color="red")
plt.title("Number of Netflix Releases Over the Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

df.to_csv("netflix_analysis.csv", index=False)

!git clone https://github.com/PravalikaJedla77/netflix-dashboard.git
!mv netflix_analysis.csv netflix-dashboard/
!cd netflix-dashboard && git add .
!cd netflix-dashboard && git commit -m "Added Netflix analysis"
!cd netflix-dashboard && git push origin main

echo "# Netflix Data Analysis Dashboard" > README.md